# INCOME TAX
TAX_CODES = {
    'L': "Standard Tax Rates",
    'M': "Marriage Allowance - 10% Allowance transferred from Spouse",
    'N': "Marriage Allowance - 10% Allowance transferred to Spouse",
    'T': "Other Calculations",
    '0T': "No Personal Allowance",
    'BR': "Taxed at Basic Rate",
    'D0': "Taxed at Higher Rate",
    'D1': "Taxed at Additional Rate",
    'D2': "Taxed at Advanced Rate (Scotland)",
    'D3': "Taxed at Top Rate (Scotland)",
    'K': "Allowance goes down by amount in prefix",
    'NT': "No Tax"
}

COUNTRY_CODES = {
    'Scotland': 'S',    # Resident in Scotland
    'Wales': 'C',   # Resident in Wales
}

EMERGENCY_CODES = {
    'W1': "Calculated Weekly",
    'M1': "Calculated Monthly",
    'X': "Calculated based on salary frequency"
}

BASIC_TAX_ALLOWANCE = 12570
ADDITIONAL_RATE_ALLOWANCE = 100000

ENGLAND_INCOME_TAX_RATES = [
    0,      # Depends on tax allowance
    0.2,    # BASIC RATE
    0.4,    # HIGHER RATE
    0.45,   # ADDITIONAL RATE
]

ENGLAND_INCOME_TAX_BRACKET = [
    [0, 1047.5, 0],      # Base, taxed at 0
    [1047.50, 4189.17, 1],   # Basic rate
    [4189.17, 10428.33, 2],  # Higher rate
    [(10428.33, float('inf'), 3)]  # Additional rate
]
# NATIONAL INSURANCE TAX
CATEGORY_LETTERS = [
    'A',    # Everyone apart from B, C, H, J, M, N, V and Z
    'B',    # Married women and widows with NIN reduction
    'C',    # Over state pension
    'D',    # Investment Zones, paid in another job
    'E',    # Investment Zones Married women/widows
    'F',    # Freeports apart from I, L, and S
    'H',    # Apprentices under 25
    'I',    # Married woman/Widows working in freeports
    'J',    # Payed in another job
    'K',    # Investment Zones, pension age
    'L',    # Working in freeports payed in another job
    'M',    # Under 21s
    'N',    # Investment zones excluding E, D and K
    'S',    # Working in freeports over state pension
    'V',    # First job after leaving armed forces (veterans)
    'Z',    # Under 21s payed in another job
    'X',    # No tax
]

NATIONAL_INSURANCE_BRACKET = {
    0: [0, 533],
    1: [533, 1048],
    2: [1048, 4189],
    3: [4189, 4189]
}

NATIONAL_INSURANCE_RATES = {
    'A': [0, 0, 0.08, 0.02],
    'B': [0, 0, 0.0185, 0.02],
    'C': [0, 0, 0, 0],
    'D': [0, 0, 0.02, 0.02],
    'E': [0, 0, 0.0185, 0.02],
    'F': [0, 0, 0.08, 0.02],
    'H': [0, 0, 0.08, 0.02],
    'I': [0, 0, 0.0185, 0.02],
    'J': [0, 0, 0.02, 0.02],
    'K': [0, 0, 0, 0],
    'L': [0, 0, 0.02, 0.02],
    'M': [0, 0, 0.08, 0.02],
    'N': [0, 0, 0.08, 0.02],
    'S': [0, 0, 0, 0],
    'V': [0, 0, 0.08, 0.02],
    'Z': [0, 0, 0.02, 0.02],
}

# STUDENT LOAN
LOAN_PLAN_RATES = {
    'Plan 1': 0.09,
    'Plan 2': 0.09,
    'Plan 4': 0.09,
    'Plan 5': 0.09,
    'Postgraduate': 0.06,
}

LOAN_PLAN_THRESHOLDS = {
    'Plan 1': 24990,
    'Plan 2': 27295,
    'Plan 4': 31395,
    'Plan 5': 25000,
    'Postgraduate': 21000,
}