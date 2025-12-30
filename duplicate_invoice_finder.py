# Import libraby
import pandas as pd

# Load CSV file
df = pd.read_csv("invoices.csv")

# Find duplicate invoices based on invoice no.
duplicates = df[df.duplicated(subset="InvoiceNo", keep=False)]

# Save duplicate invoices to CSV
duplicates.to_csv("duplicate_invoices.csv", index=False)

# Remove duplicates to create clean data
clean_data = df.drop_duplicates(subset="InvoiceNo", keep="first")

# Save Clean invoices to CSV
clean_data.to_csv("clean_invoices.csv", index=False)

# confirmation message
print("Duplicate and clean invoice files created successfully")


