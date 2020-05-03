import RelatedSearches
related_searches_list = RelatedSearches.myFunction("US Dollar price")
print(related_searches_list)
import tweetScrapeAndSave
tweetScrapeAndSave.tweetScrapeFunction(related_searches_list)
import testModel
finalResult = testModel.final_result_achieved
print("Final Result : ", finalResult)