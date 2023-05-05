# GmailApi
## TODO
  `pip install -r requirements`


   Firstly, run `python gmail_to_db`
   
   1. Google Mail API API authentication with OAuth 2
    ![Picture2](https://user-images.githubusercontent.com/72887609/236460390-fa7ae6d1-184d-4ff5-af39-2dd5a4779e58.png)
   2. Get `credentials.json` from the google cloud platform.
   3. This script will call the `authenticate_service() ` from the `gmail_scraper` file.
   4. After the successfully authentication, `token.json / token.pickle` file will be created automatically.
   
   ## Storing in Postgres
   Create a New Database named `Gmailapi` and create a new Table in pgAdmin4.
          
    To view the table `SELECT id,email_id,from_email,to_email,subject,send_on FROM "public".MAILS m; `
  
  ![Picture3](https://user-images.githubusercontent.com/72887609/236476090-2595c267-301f-4192-b02f-3574507a75dd.png)


4. ` actions_on_gmail.py ` - Performing the actions on gmail based on certain conditions in the `rules.json` file.
