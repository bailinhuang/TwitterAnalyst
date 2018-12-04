var word_range = 3;
var cursor = db.tweets_lgbt_old.aggregate([{$project : {"splitted_tweet" : {$split : ["$text"," "]},"_id" :0 }}]);
//var corpus = db.corpus.find({},{"array":1,"_id":0}).toArray()[0].array;
var corpus = ["el", "los", "la", "las", "un", "unos", "una", "unas", "al", "del", "lo", "y", "o", "e", "u", "de", "para", "a", "con", "en", "desde", "durante", "hacia", "hasta", "por", "según", "tras", "!"]

while ( cursor.hasNext() ) {
	var current_tweet = cursor.next();
	var splitted_tweet = current_tweet.splitted_tweet
	var lgbt_index = splitted_tweet.indexOf("lgbt");
	var left_counter = 0;
	var right_counter = 0;
	var current_index = lgbt_index - 1;
	while((left_counter < word_range) && (current_index >= 0)){
		current_word = splitted_tweet[current_index];
		if (-1 == corpus.indexOf(current_word)){
			if (0 == db.lgbt_word_freq_old.find({"_id":current_word}).count()) {
				db.lgbt_word_freq_old.insert({"_id" : current_word, "freq" : 1})
			} else {
				db.lgbt_word_freq_old.update({"_id" : current_word},{$inc : {"freq" : 1}})
			}
			left_counter += 1;
		}
		current_index -= 1;
	}
	current_index = lgbt_index + 1;
	while((right_counter < word_range) && (current_index < splitted_tweet.length)){
		current_word = splitted_tweet[current_index];
		if (-1 == corpus.indexOf(current_word)){
			if (0 == db.lgbt_word_freq_old.find({"_id":current_word}).count()) {
				db.lgbt_word_freq_old.insert({"_id" : current_word, "freq" : 1})
			} else {
				db.lgbt_word_freq_old.update({"_id" : current_word},{$inc : {"freq" : 1}})
			}
			right_counter += 1;
		}
		current_index += 1;
	}
	//printjsononeline(splitted_tweet[lgbt_index]);
} 