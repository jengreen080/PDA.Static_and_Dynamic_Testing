# define a function with the parameter of a new country
# define the sql table and columns to save information to while requesting sql to return the corresponding country_id it assigns to the inputed information
# define the values to be inputted to the sql table
# define a variable called results. make this equal to the output of the run_sql file
# define a variable, country_id, as the information returned from index 0 of the list. 
# set the id of the Country class to be equal to the country_id variable
# return the saved new country to save the data


def save(country):
    sql = "INSERT INTO countries (country_name, continent) VALUES (%s, %s) RETURNING country_id"
    values = [country.country_name, country.continent]
    results = run_sql(sql, values)
    country_id = results[0]["country_id"]
    country.country_id = country_id
    return country


