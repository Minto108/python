def generate_sentences(subjects,verbs,objects):
	return [x +" " + y + " " + z for x in subjects for y in verbs for z in objects]

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))