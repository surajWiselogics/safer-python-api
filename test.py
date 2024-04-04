from safer import CompanySnapshot

client = CompanySnapshot()
company = client.get_by_usdot_number(1590983)
print(company.to_json())