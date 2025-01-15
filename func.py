import definitions as dfs
import copy

class Set_Up_Calculator:
    """
    A class to calculate tax information based on salary and tax code
    """

    def __init__(
            self,
            base_salary: int,
            tax_code: str = '1257L',
            wage_format: str = 'yearly',
            week: float = 52,
            national_insurance_category: str = 'A',
            student_loan_plan: list = None,
            pension_amount: int = 0,
            pension_rate: float = 0,
            bonus_amount: int = 0,
            bonus_rate: float = 0,
    ):

        """
        Initialise the Salary Calculator
        :param base_salary: Base salary (yearly/monthly/weekly)
        :param tax_code: Determines tax rates, bands and allowances
        :param wage_format: Format with which salary was input (yearly/monthly/weekly)
        :param week: Number of weeks in a year 52 or 52.143
        :param national_insurance_category: Category used to apply rate
        :param student_loan_plan: Can take up values Plan 1, Plan 2, Plan 4 (Scotland), Plan 5 or Postgraduate
        :param pension_amount: Pension amount nominal
        :param pension_rate: Pension rate in % to pay before tax
        :param bonus_amount: Amount of annual bonus
        :param bonus_rate: Annual bonus rate
        """

        # Attributes
        self.base_salary = base_salary
        self.tax_code = tax_code.upper()
        self.wage_format = wage_format
        self.week = week
        self.national_insurance_category = national_insurance_category
        self.student_loan_plan = student_loan_plan
        self.pension_amount = pension_amount
        self.pension_rate = pension_rate
        self.bonus_amount = bonus_amount
        self.bonus_rate = bonus_rate

    def convert_salary_frequency(self):
        """
        Convert to monthly salary
        :return: monthly salary
        """
        # Convert Salary to yearly and monthly
        if self.wage_format == 'yearly':
            base_salary_monthly = round(self.base_salary / 12, 2)
            return base_salary_monthly
        elif self.wage_format == 'monthly':
            base_salary_monthly = self.base_salary
            return base_salary_monthly
        elif self.wage_format == 'weekly':
            base_salary_monthly = round((self.base_salary * self.week) / 12, 2)
            return base_salary_monthly

    def get_total_yearly_salary(self):
        """
        Calculates the total yearly salary
        :return:
        """
        total_yearly_salary = (self.base_salary_monthly * 12) # to add other functions
        return total_yearly_salary

    def get_tax_code_letter(self):
        """
        Retrieve the tax code to use for income tax calculation

        :return: tax code from dictionary TAX_CODES
        """
        for tax_code_letter in dfs.TAX_CODES.keys():
            if tax_code_letter in self.tax_code:
                return tax_code_letter

    def get_tax_allowance(self):
        """
        Extract the numeric part of a tax code
        :return: Numeric part as an integer, multiplied by 10
        """
        # Handle normal cases tax codes: L, M, N, T, K,
        tax_code_letter = self.get_tax_code_letter()
        if tax_code_letter in ['L', 'M', 'N', 'T', 'K']:
            # Split tax code into parts (e.g. 1257L M1 -> ['1257L', 'M1'], removing emergency tax codes
            tax_code_split = self.tax_code.split()
            main_tax_code = tax_code_split[0]

            # Iterate over dictionary to find a match a remove it from string
            for key in dfs.TAX_CODES.keys():
                main_tax_code = main_tax_code.replace(key, "")

            # Handle K tax code
            if tax_code_letter == 'K':
                allowance = 12570 - (int(''.join(filter(str.isdigit, main_tax_code))) * 10)
                return allowance / 12

            # Handle L, M, N, T tax codes
            else:
                allowance = int(''.join(filter(str.isdigit, main_tax_code)))
                return allowance * 10 / 12 if allowance else None

        # For all other tax codes
        else:
            allowance = 0
            return allowance

    def get_emergency_code(self):
        """
        Identifies and returns emergency codes
        :return: Emergency code (e.g. M1, W1)
        """
        tax_code = self.tax_code
        for key in dfs.EMERGENCY_CODES.keys():
            if key in tax_code:
                emergency_code = tax_code.split()[-1]
                return emergency_code

    def get_pension(self):
        """
        Calculates pention amount
        :return: pension amount in £
        """
        pension_amount = self.pension_amount
        pension_rate = self.pension_rate / 100
        base_salary = self.convert_salary_frequency()

        if pension_amount != 0:
            return pension_amount
        elif pension_rate != 0:
            pension = pension_rate * base_salary
            return pension
        else:
            pension = 0
            return pension

    def get_bonus(self):
        """
        Calculates bonus amount
        :pension rate if pension amount is not inputted
        :return: bonus amount yearly in £
        """
        bonus_amount = self.bonus_amount
        bonus_rate = self.bonus_rate / 100
        base_salary = self.convert_salary_frequency() * 12

        if bonus_amount != 0:
            return bonus_amount
        elif bonus_rate != 0:
            bonus = bonus_rate * base_salary
            return bonus
        else:
            bonus = 0
            return bonus

    def get_salary_sacrifice(self):
        pass

    def get_overtime(self):
        pass

    def get_taxable_benefits(self):
        pass

    def get_childcare_benefits(self):
        pass

    def get_student_loan(self):
        pass

    def get_country_code(self, country=None):
        """
        Returns the country code for
        :param country: country of residency
        :return:
        """
        tax_code = self.tax_code
        if country is None:
            for value in dfs.COUNTRY_CODES.values():
                if value in tax_code:
                    return value
            return None
        else:
            if country == "Northern Ireland":
                print("Equivalent to english tax code")
                return None
            elif country == "Scotland" or country == "Wales":
                return dfs.COUNTRY_CODES[country]
            return None

    def calculate_salary_with_deductions(self, pension=0, bonus=0):  # to add other factors (e.g. student loans)
        """
        Calculates the amount of income that can be taxed after deductions
        :param pension: Pension to be taken out of total salary
        :param bonus: Bonus to be added to a single month
        :return: Total taxable salary
        """
        base_salary = self.convert_salary_frequency()
        base_salary = base_salary - pension

        if bonus == 0:
            return base_salary
        else:
            bonus_month = base_salary + bonus
            return base_salary, bonus_month
        pass

    def calculate_income_tax(self, salary_with_deductions, allowance, country=None, bonus=0):
        """
        :param salary_with_deductions:
        :param allowance:
        :param country:
        :param bonus: 0 for bonus 1 for no bonus
        :return:
        """
        tax_bracket = 0
        income_tax = 0
        tax_code_letter = self.get_tax_code_letter()

        if country is None or country == 'C':

            # Calculate tax codes L, M, N, T and K
            if tax_code_letter in ['L', 'M', 'N', 'T', 'K']:
                if bonus == 0:

                    # Calculate bracket
                    for lower, upper, bracket in dfs.ENGLAND_INCOME_TAX_BRACKET:
                        if lower < salary_with_deductions <= upper:
                            tax_bracket = bracket
                            break
                    print(bracket)
                    # Calculate income tax
                    if bracket == 0 or salary_with_deductions == 0:
                        return 0
                    elif bracket > 0:
                        pass

                    # Calculate tax
                    pass
        else: # Add Scotland
            pass
        pass
