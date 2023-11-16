from random import randint
from faker import Faker


class FakeData:
    @property
    def first_name(self):
        return Faker().first_name()

    @property
    def last_name(self):
        return Faker().last_name()

    @property
    def email(self):
        return Faker().email()

    @property
    def password(self):
        return Faker().password()

    @property
    def phone_number(self):
        return Faker().phone_number()

    @property
    def postcode(self):
        return Faker().postcode()

    @property
    def secondary_address(self):
        return Faker().secondary_address()

    @property
    def street_address(self):
        return Faker().street_address()

    @property
    def city(self):
        return Faker().city()

    @property
    def state(self):
        return Faker().state()

    def us_postcode_state(self, state):
        """Необходимо указать полное название штата что бы получить почтовый индекс этого штата"""
        converter = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
                     'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
                     'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
                     'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                     'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
                     'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                     'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
                     'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                     'South Carolina': 'SC',
                     'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                     'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI',
                     'Wyoming': 'WY'}
        state = converter[state]
        return Faker().postcode_in_state(f'{state}')

    @property
    def fake_order_id(self):
        fake_order_id = randint(111111111, 999999999)
        return fake_order_id
