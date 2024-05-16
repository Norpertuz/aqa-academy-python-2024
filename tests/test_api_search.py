def test_check_search_repo(git_hub_api_client):
    """
    1. send API request to find the repo named NAME
    2. Analyse the responce

    Expected result:
    number of found repos == SOMENUMBER
    """

    # 1. send API request to find the repo named NAME
    repos_number, response = git_hub_api_client.search_repos("sergii")
    watcher_count, response_two = git_hub_api_client.get_repo_info(
        owner="Norpertuz", repo_name="AdaptiveGallery"
    )
    responses = [response, response_two]

    # 2. Analyse responses
    #
    # for res in responses:
    #    if res.status != 200:
    #        raise Exception("Bad request")
    #
    response.raise_for_status()

    assert repos_number == 352
    assert watcher_count == 1
