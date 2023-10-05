import json
import os


class Orm:
    users_dir = 'users'

    @staticmethod
    def loading(parent):
        f_name = os.path.join(Orm.users_dir, f"{parent.name}.json")
        with open(f_name, 'r', encoding='utf-8') as f_json:
            load_dict = json.load(f_json)
        return load_dict

    @staticmethod
    def saving(parent, save_dict):
        f_name = os.path.join(Orm.users_dir, f"{parent.name}.json")
        with open(f_name, 'w', encoding='UTF-8') as f_json:
            json.dump(save_dict, f_json, indent=4)




