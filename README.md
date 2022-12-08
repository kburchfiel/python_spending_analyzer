# Python Spending Analyzer
This project shows how to use Python to (1) aggregate and code personal financial statements (e.g. from credit and debit card providers) and (2) analyze spending on a monthly and annual basis. 

## Introduction
When I was growing up, my dad would get me to code our family’s financial transactions so that he could analyze how our family was spending its money. When I first began doing this, I would have to type in dates and transactions from paper statements. Later on, I was able to download these statements from banking websites, which made the process much faster. 

However, even with electronic statements in place, I still needed to spend a good amount of time manually coding expenses. My dad had codes for grocery store purchases, car maintenance, travel, taxes, and many other transaction types. Sorting my Excel spreadsheet by description and then entering in these codes by hand took a good amount of time.

Now that I’m living on my own, I still want to keep track of my spending. Therefore, I decided to try to make the coding process faster by creating a Python project that could automatically code many expenses. Some manual input is still necessary, but I expect that my script will make my financial analyses much faster in the future. As an added benefit, the project incorporates Plotly to create both interactive and static charts.

Online programs like Mint have made it easier than ever to track your finances without much effort on your end. However, using Python to track your expenses still has certain benefits. You can base your analysis off your own codes and subcodes from the very beginning, and you can apply Plotly to get full control of the spending visualization process.

## How the Program Works
The project’s scripts contain detailed information about how the program operates, so I’ll keep my description here pretty brief. 

The project relies on two scripts. The first script, financial_statements_coding_tool, reads financial statements (which you’ll need to download beforehand from your bank and/or credit card provider) into a Pandas DataFrame. It then uses your own list of description-code pairs to automatically code a portion of these transactions. 

(For instance, suppose your rent payments always have the description “Evergreen Apartments Rent Payment” in your financial statements. If you assign the code H-R (short for Home—Rent) to those statements, the script would then place an ‘H-R’ subcode next to each instance of your rent payment description. This will all make more sense when you look at the actual code.)

The script concludes by exporting a partially coded version of your financial transactions data to a .csv file. Next, you’ll probably need to do some manual work to fill in the gaps that your program couldn’t code on its own. For instance, suppose many of your transactions are from DiscountsOnline.com and have only ‘DiscountsOnline’ in their description. If you buy all sorts of things (clothes, books, cookware, food, car parts, etc.) from this store, you won’t be able to successfully categorize these expenses using the description alone. Instead, you’ll need to go into your purchase history and manually categorize each purchase (using the date and amount as a reference). 

Once you’ve coded all of your expenses, you can then import this edited .csv file into financial_statements_analyzer. This script will merge your coded expenses together with a .csv file containing your financial codes. (You can use the sample_finance_codes.csv file as a starting point.) It will then use Plotly to create both interactive (.html) and static (.png) graphs showing your annual expenses by code and subcode and your monthly expenses by code. (Note that the interactive charts probably won’t appear within GitHub; instead, you’ll need to download the project and view the .html charts by opening them in a web browser.) 

To illustrate how this program works, I provide two fictional bank and credit card statements in the simulated_spending_data folder. The data shown in the folder does not represent actual financial data. 

Currently, I have only analyzed data from one year using this program. However, in future years, I may modify the code so that it can import and visualize data from multiple years. That way, I’ll be able to see how my expenses change from one year to another.

I hope you’ll find this project as useful as I have for analyzing your own finances!
