def savings(gross_pay, tax_rate, expenses):
    '''Savings.

    This function calculates the money remaining
        for an employee after taxes and expenses.

    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    after_tax_pay = int(gross_pay * (1 - tax_rate))  # Using int() to round down
    
    remaining_savings = after_tax_pay - expenses
    
    return remaining_savings

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.

    This function calculates how much material will be left after running
    a certain number of jobs that consume a specific amount of material.

    To figure out the waste:
        1. Multiply the number of jobs by the material each job uses.
        2. Subtract that from the total material available to see how much is left.

    You'll get the result as a string with the unit attached (no space between the number and unit).

    Parameters
    ----------
    total_material: int
        The total material you have
    material_units: str
        The units for the material (like "kg", "L", etc.)
    num_jobs: int
        How many jobs you're running
    job_consumption: int
        How much material one job uses

    Returns
    -------
    str
        The leftover material, with the unit attached (e.g., "10kg").
    '''
    
    total_used = num_jobs * job_consumption
    
    remaining_material = total_material - total_used
    
    return f"{remaining_material}{material_units}"

def interest(principal, rate, periods):
    '''Interest.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal by the quantity (rate * time).
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    
    interest = principal * rate * periods
    
    final_value = principal + interest
    
    return int(final_value)