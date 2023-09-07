## Source Data 

Part of the English corpus from [CC-100](https://data.statmt.org/cc-100/). 

## Size 

A total of around 110,000 English-Amharic sentence pairs. 

## Method 

 Back-translation using [Google's Cloud Translation API](https://cloud.google.com/translate/). The API was first used to translate the English sentences to Amharic. Then again to translate the Amharic sentences to English. The original English sentence and the back-translated one were then compared using [sentence transformers](https://www.sbert.net/). Sentences with similarity score of more than 0.9 were included in the parallel corpus. 

 ## Examples 

 ```
Thanks Rebecca for sharing this recipe, it sounds great and I can’t wait to try it!!
ይህን የምግብ አሰራር ስላጋራሽ እናመሰግናለን ርብቃ በጣም ጥሩ ይመስላል እና እስክሞክር ድረስ መጠበቅ አልችልም!!

Love this recipe, tried it last night with cauliflower rice and it was delicious!!!!!!
ይህን የምግብ አሰራር ወደዱት ፣ ትላንትና ማታ ከአበባ ጎመን ሩዝ ጋር ሞክረው ጣፋጭ ነበር!!!!!!

I am adding a mint chutney recipe with my post try it with butter chicken,you will love it-
ከጽሁፌ ጋር አንድ ሚንት ቹቲኒ አሰራር እጨምራለሁ በቅቤ ዶሮ ሞክሩት ትወዱታላችሁ-

I am new to this and this may be a stupid question, but what is califlower rice?
እኔ ለዚህ አዲስ ነኝ እና ይህ ምናልባት የሞኝነት ጥያቄ ሊሆን ይችላል, ግን የካሊፎር ሩዝ ምንድን ነው?
 ```

 ## Limitations 

  - The free version of the API was used and it only supported around 130k * 2 translations. 
  - It was very much time consuming, the total time taken to make these 110k sentence pairs was around 12 hours running on Google Cloud's console itself. (Because of issues with installing the Google Cloud command line tool.)
   - Some translation might be wrong twice and result in wrong translations being included in the parallel corpus. 


## Usage 

- Go to Google's Cloud Translation API page (https://cloud.google.com/translate/), follow the instructions to create your accound and get an API key, install the Google Cloud SDK (if you will work locally). 
- Prepare an English corpus (line by line).
- Modify the ```source_file_path``` and the ```parallel_file_path``` in the ```back_translation.py``` file. 
- Run the following command:
```
python back_translation.py
```