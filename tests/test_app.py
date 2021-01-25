import unittest
import env
import os
from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
from bson import ObjectId as mockup_oid
from json import dumps
from pymongo import MongoClient

from app import app

recipe = {
    "category_name": "Cocktails",
    "recipe_name": "Gin and Tonic",
    "recipe_description": "",
    "is_vegetarian": "off"
}


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # create mongo connection to mock server
        app.testing = True
        self.mongo_client = MongoClient(os.environ.get('TEST_MONGODB_URI'))
        self.app = app.test_client()
        self.db = self.mongo_client['test_recipe_manager']
        self.recipes_coll = self.db['recipes']
        self.allergens_coll = self.db['allergens']
        self.users_coll = self.db['users']

    @classmethod
    def tearDownClass(self):
        # TODO: Make sure the dabasabe is deleted. No working at the moment
        # raise OperationFailure(errmsg, code, response, max_wire_version)
        # pymongo.errors.OperationFailure: user is not allowed to do action 
        # [dropDatabase] on [test_recipe_manager.], 
        # full error: {'ok': 0, 'errmsg': 'user is not allowed to do action 
        # [dropDatabase] on [test_recipe_manager.]', 'code': 8000, 
        # 'codeName': 'AtlasError'}

        # self.mongo_client.drop_database('test_recipe_manager')
        pass

    def test_insert_recipe(self):
        self.recipes_coll.remove()
        self.recipes_coll.insert_one(recipe)
        number_recipes = self.recipes_coll.find().count()
        self.assertEqual(number_recipes, 1)

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post_recipe(self):
        with self.app.session_transaction() as sess:
            sess['user'] = 'Fabian'
            response = self.app.post('/add_recipe', data=dict(recipe),
                                     follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            print(response)


if __name__ == '__main__':
    unittest.main()
