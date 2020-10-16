# Automated RSS reporter bot for Telegram

### Requriements
- Python 3.6
- Docker
- Telegram account
- Microsoft Azure account

------------


### Configuration & setup
1. Create a Telegram bot. For detailed instructions, check [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot "here").

2. Note the **bot token** and **channel ID**, and manually update them in the `config.json` file. Also put all your RSS feed links in that file. Note: this might require additional code changes in the `bot.py` file regarding the parsing of the feed file, since some formats differ from others.

3. This might be a good time to test your bot by running the python script manually.

4. Login to Azure Portal and create a container registry. Give it a name, subscription, resource group and location. Note the following information:
    - Resource Group Name
	- Login Server

   You can run the `deploy.sh `after modifiying the commands or follow the steps below:

5. Build the docker image:

   `docker build -t <mycontainer>.azurecr.io/worker:v0.1 .`

6. Login to your Azure container registry

   ` docker login <mycontainer>.azurecr.io`

7. Push the docker image to your Azure container registry

   `docker push <mycontainer>.azurecr.io/worker:v0.1`

8. Now you need to create an Automation Account (Search for *Automation Accounts > Add*). 

   To use the latest version of Azure CLI for operations with containers, we need to install specific modules. But first, we need to update the modules. Go to *RunBooks > Import a runbook* and select `Update-AutomationAzureModulesForAccount.ps1`. Save, Publish & run the script.

   Once done, go to *Modules > Browse Gallery* and the modules **AzureRM.ContainerInstance** and **AzureRM.ContainerRegistry**.

9. Create another runbook which will create our container and run the python script. Import the `AutomationContainer.ps1` after updating the appropirate parameters, mainly the **Resource Group Name**, the **Container Registry Name** and **Image Name**.

10. Save, Publish and start the runbook to test it.

11. Finally, you can link the webhook to a schedule so your script can run periodically.
