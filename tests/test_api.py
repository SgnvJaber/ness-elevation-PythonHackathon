import allure
from configuration.conftest import *
from main.extensions import verifications
from main.workflows.api_flows import Api_Flows


@pytest.mark.usefixtures('init_api')
class Test_Api:

    @allure.title("Verify post new song success")
    @allure.step("Verify we are able to add new song.")
    def test_post(self):
        verifications.verify_equals(Api_Flows.add_new_song(Common_Ops.get_data('newSongAuthor'),
                                                           Common_Ops.get_data('newSongName'),
                                                           Common_Ops.get_data('newSongYear')), 201)

    @allure.title("Verify get all data from specific category")
    @allure.step("Make sure the data printed out is all of the songs")
    def test_get(self):
        verifications.verify_equals(Api_Flows.get_data_based_category(
            Common_Ops.get_data('searchByCategory')), 200)

    @allure.title("Verify updating partial data at specific id")
    @allure.step("By sending id and some data, we ar updating the data at that specific id, make sure it's success")
    def test_patch(self):
        verifications.verify_equals(Api_Flows.patch_songs_data("songs",
                                                               Common_Ops.get_data('songID'),
                                                               Common_Ops.get_data('newAuthorNameForPatch'),
                                                               Common_Ops.get_data('newSongNameForPatch')), 200)
