import numpy as np

from sklearn.externals import joblib


MODEL_PATH = 'logic_application/model.pkl'


class Network:

    def __init__(self, model_path=MODEL_PATH):
        self.model = joblib.load(model_path)

    def predict(self, user_input):
        a = self.input_to_one_hot(user_input)
        price_pred = self.model.predict([a])[0]
        price_pred = round(price_pred, 2)
        return {'price': price_pred}

    @staticmethod
    def input_to_one_hot(data):
        # initialize the target vector with zero values
        enc_input = np.zeros(61)
        # set the numerical input as they are
        enc_input[0] = data['year_model']
        enc_input[1] = data['mileage']
        enc_input[2] = data['fiscal_power']
        # get the array of marks categories
        marks = ['Peugeot', 'Renault', 'Citroen', 'Mercedes-Benz', 'Ford', 'Nissan',
                 'Fiat', 'Skoda', 'Hyundai', 'Kia', 'Dacia', 'Opel', 'Volkswagen',
                 'mini', 'Seat', 'Isuzu', 'Honda', 'Mitsubishi', 'Toyota', 'BMW',
                 'Chevrolet', 'Audi', 'Suzuki', 'Ssangyong', 'lancia', 'Jaguar',
                 'Volvo', 'Autres', 'BYD', 'Daihatsu', 'Land Rover', 'Jeep', 'Chery',
                 'Alfa Romeo', 'Bentley', 'Daewoo', 'Hummer', 'Mazda', 'Chrysler',
                 'Maserati', 'Cadillac', 'Dodge', 'Rover', 'Porsche', 'GMC',
                 'Infiniti', 'Changhe', 'Geely', 'Zotye', 'UFO', 'Foton', 'Pontiac',
                 'Acura', 'Lexus']
        cols = ['year_model', 'mileage', 'fiscal_power', 'fuel_type_Diesel',
                'fuel_type_Electrique', 'fuel_type_Essence', 'fuel_type_LPG',
                'mark_Acura', 'mark_Alfa Romeo', 'mark_Audi', 'mark_Autres', 'mark_BMW',
                'mark_BYD', 'mark_Bentley', 'mark_Cadillac', 'mark_Changhe',
                'mark_Chery', 'mark_Chevrolet', 'mark_Chrysler', 'mark_Citroen',
                'mark_Dacia', 'mark_Daewoo', 'mark_Daihatsu', 'mark_Dodge', 'mark_Fiat',
                'mark_Ford', 'mark_Foton', 'mark_GMC', 'mark_Geely', 'mark_Honda',
                'mark_Hummer', 'mark_Hyundai', 'mark_Infiniti', 'mark_Isuzu',
                'mark_Jaguar', 'mark_Jeep', 'mark_Kia', 'mark_Land Rover', 'mark_Lexus',
                'mark_Maserati', 'mark_Mazda', 'mark_Mercedes-Benz', 'mark_Mitsubishi',
                'mark_Nissan', 'mark_Opel', 'mark_Peugeot', 'mark_Pontiac',
                'mark_Porsche', 'mark_Renault', 'mark_Rover', 'mark_Seat', 'mark_Skoda',
                'mark_Ssangyong', 'mark_Suzuki', 'mark_Toyota', 'mark_UFO',
                'mark_Volkswagen', 'mark_Volvo', 'mark_Zotye', 'mark_lancia',
                'mark_mini']

        # redefine the the user inout to match the column name
        redefinded_user_input = 'mark_' + data['mark']
        # search for the index in columns name list
        mark_column_index = cols.index(redefinded_user_input)
        # print(mark_column_index)
        # fullfill the found index with 1
        enc_input[mark_column_index] = 1
        ##################### Fuel Type ####################
        # get the array of fuel type
        fuel_type = ['Diesel', 'Essence', 'Electrique', 'LPG']
        # redefine the the user inout to match the column name
        redefinded_user_input = 'fuel_type_' + data['fuel_type']
        # search for the index in columns name list
        fuelType_column_index = cols.index(redefinded_user_input)
        # fullfill the found index with 1
        enc_input[fuelType_column_index] = 1
        return enc_input
