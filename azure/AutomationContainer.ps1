Import-Module Azure
Import-Module AzureRm.ContainerRegistry
Import-Module AzureRm.ContainerInstance

$connectionName = "AzureRunAsConnection"
$resGroup = "MyResGroup"
$containerRegistryName = "ayabot"
$imageName = "ayabot.azurecr.io/worker:v0.1"
try
{
    # Get the connection "AzureRunAsConnection "
    $servicePrincipalConnection=Get-AutomationConnection -Name $connectionName         

    "Logging in to Azure..."
    Add-AzureRmAccount `
        -ServicePrincipal `
        -TenantId $servicePrincipalConnection.TenantId `
        -ApplicationId $servicePrincipalConnection.ApplicationId `
        -CertificateThumbprint $servicePrincipalConnection.CertificateThumbprint 
}
catch {
    if (!$servicePrincipalConnection)
    {
        $ErrorMessage = "Connection $connectionName not found."
        throw $ErrorMessage
    } else{
        Write-Error -Message $_.Exception
        throw $_.Exception
    }
}

$cred = Get-AzureRmContainerRegistryCredential -ResourceGroupName $resGroup -Name $containerRegistryName
$secPassword = ConvertTo-SecureString $cred.Password -AsPlainText -Force
$acrCred = New-Object System.Management.Automation.PSCredential($containerRegistryName, $secPassword)

New-AzureRmContainerGroup -ResourceGroupName $resGroup -Name worker -Image $imageName -OsType Linux -RegistryCredential $acrCred -RestartPolicy Never

Start-Sleep 120

while($true) {
    if ( (Get-AzureRmContainerInstanceLog -ResourceGroupName $resGroup -ContainerGroupName worker) -eq "Uploading to blob`n") {
        Remove-AzureRmContainerGroup -ResourceGroupName $resGroup -Name worker
        Write-Output "Container removed"
        Break
    }
    Start-Sleep 10
}
