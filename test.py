from safer import CompanySnapshot

client = CompanySnapshot()

results = client.search('python')
company = results[0].get_company_snapshot()
print(company.legal_name)