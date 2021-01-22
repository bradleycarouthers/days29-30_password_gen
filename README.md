# days29-30_password_gen
Days 29 and 30 of 100.

Today I had my initial exposure to .json files. Worked with loading, dumping, and updating. Also, gained experience with catching exceptions using try-except-else-finally.

When the file is ran the first time, a .json file is created with relevant information that has been written to it. The functionality allows the user to search for a website they may have saved before. However, if this function is used before the .json file is even created, there will be an error message. So, after saving a few sites, emails, and passwords, the user can input a certain website name and click the search button. When they do, a message box pops up with the associated information.

But we all make mistakes and maybe the user is looking for a website that has not been saved yet. In that case, instead of crashing, the exception is caught and you get an error message, f"No details for {website} exist".
