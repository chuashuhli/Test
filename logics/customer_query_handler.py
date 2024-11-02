import json
from helper_functions import llm

# Load the JSON file
filepath = './data/typeofsocialassistance-full.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_assistance = json.loads(json_string)

category_n_assistance_name = {
    "Short-To-Medium Term": ["ComCare Short-to-Medium-Term Assistance (SMTA)"],
    "Immediate Social Assistance": ["ComCare Long Term Assistance (LTA)"],
    "Long-Term Social Assistance": ["ComCare Interim Assistance"]
}

def identify_category_and_assistances(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant to any specific assistance programs
    in the Python dictionary below, where each key is a `category`
    and the value is a list of `assistance_name`.

    If there are any relevant assistance program(s) found, output the pair(s) of a) `assistance_name` the relevant programs and b) the associated `category` into a
    list of dictionary object, where each item in the list is a relevant program
    and each program is a dictionary that contains two keys:
    1) category
    2) assistance_name

    {category_n_assistance_name}

    If no relevant assistance programs are found, output an empty list.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"}
    ]
    category_and_product_response_str = llm.get_completion_by_messages(messages)
    category_and_product_response_str = category_and_product_response_str.replace("'", "\"")
    category_and_product_response = json.loads(category_and_product_response_str)
    return category_and_product_response

def get_assistance_details(list_of_relevant_category_n_assistance: list[dict]):
    assistance_names_list = []
    for x in list_of_relevant_category_n_assistance:
        assistance_names_list.append(x.get('assistance_name')) # x["assistance_name"]

    list_of_assistance_details = []
    for assistance_name in assistance_names_list:
        list_of_assistance_details.append(dict_of_assistance.get(assistance_name))
    return list_of_assistance_details

def generate_response_based_on_assistance_details(user_message, assistance_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about assistance programs, \
    understand the relevant program(s) from the following list.
    All available programs shown in the json data below:
    {assistance_details}

    Step 2:{delimiter} Use the information about the program to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the program information.
    Your response should be as detailed as possible and \
    include information that is useful for customer to better understand the program.

    Step 3:{delimiter} Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    customers make their decision.
    Complete with details such as eligibility, benefits, application process, and contact information.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"}
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer

def process_user_message(user_input):
    delimiter = "```"

    # Process 1: If assistance programs are found, look them up
    category_n_assistance_name = identify_category_and_assistances(user_input)
    print("category_n_assistance_name : ", category_n_assistance_name)

    # Process 2: Get the Assistance Details
    assistance_details = get_assistance_details(category_n_assistance_name)

    # Process 3: Generate Response based on Assistance Details
    reply = generate_response_based_on_assistance_details(user_input, assistance_details)

    # Process 4: Append the response to the list of all messages
    return reply