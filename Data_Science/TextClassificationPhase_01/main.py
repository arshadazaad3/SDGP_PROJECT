import RelatedSearches
user_searched_phrase = "corona"
related_searches_list = RelatedSearches.myFunction(user_searched_phrase)
print(related_searches_list)
import tweetScrapeAndSave
tweetScrapeAndSave.tweetScrapeFunction(related_searches_list, user_searched_phrase)
import testModel
finalResult = testModel.final_result_achieved
print("Final Result : ", finalResult)