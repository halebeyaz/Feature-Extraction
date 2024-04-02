from turkish.deasciifier import Deasciifier

def deascifiier(reviews):
	for review in reviews:
		for sentence in review.sentences:
			sentence.text = Deasciifier(sentence.text).convert_to_turkish()
	return reviews


