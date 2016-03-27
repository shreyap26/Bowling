def calculateScoreForFrames(game = [[]]):
	score_for_each_frame = []; 
	for i, frame in reversed(list(enumerate(game))):
		if (isLast(i) and (isStrike(frame) or isSpare(frame))):
			#print "last strike or spare" 
			if i+1 < len(game):
				#print "index: ", len(game)-i-2
				score = score_for_each_frame[len(game)-i-2] + scoreFor(frame)
				score_for_each_frame.append(score);
			else:
				score_for_each_frame.append(10)			  
		elif (isStrike(frame)):
			#print "Strike"
			if i+1 < len(game):
				#print "score before strike: ", score
				score = 10 + score_for_each_frame[i-1]
				score_for_each_frame.append(score) ;
				#print "score after strike: ", score
			else:
				score_for_each_frame.append(10)		
		elif (isSpare(frame)):
			#print "Spare"
			if i+1 < len(game):
				#print "score before spare: ", score 
				score = 10 + game[i-1][0]
				score_for_each_frame.append(score); 
				#print "score after spare: ", score
			else:
				score_for_each_frame.append(10)	
		else:
			score_for_each_frame.append(scoreFor(frame)); 

	return score_for_each_frame							  	

def calculateScoreForGame(score_for_each_frame = []):
	score = sum (score_for_each_frame); 		
	return score 

def isLast(i):
	if i==9:
		return True; 
	return False
		
def isStrike(frame=[]):
	if frame[0] == 10:
		return True; 
	return False
	
def isSpare(frame=[]):
	if scoreFor(frame) == 10:
		return True
	return False

def scoreFor(frame=[]):
	return frame[0] + frame[1]; 


if __name__ == "__main__":
	#testing a Strike Score:
	game = [[10, 0], [2, 3], [1, 8]]
	#expected 10 + 0 + 2 + 3 + 2 + 3 + 1 + 8 = 29
	#print game 
	l = calculateScoreForFrames(game)
	print "One Strike Example: \n", "Expected: 29", "Calculated: ", calculateScoreForGame(l)
	game = [[10, 0], [2, 3], [10, 0]]
	l = calculateScoreForFrames(game)
	#game ended prematurely: expected score: 30
	print "Strike ended prematurely: \n", "Expected: 30", "Calculated: ", calculateScoreForGame(l)

	#testing a Spare Score
	game = [[1, 8], [6, 4], [1, 8]]
	l = calculateScoreForFrames(game)
	#expected 1 + 8 + 6 + 4 + 1 + 1 + 8 = 29
	print "One Spare Example: \n", "Expected: 29", "Calculated: ",calculateScoreForGame(l)
	game = [[1, 8], [1, 8], [6, 4]]
	l = calculateScoreForFrames(game)
	#game ended prematurely: expected score: 28
	print "Spare Ended prematurely: \n", "Expected: 28", "Calculated: ", calculateScoreForGame(l)

	#testing Strike or Spare at 10th frame 
	game = [[2, 3], [1, 2], [3, 4], [6, 2], [1, 2], [2, 3], [3, 4], [5, 2], [1, 5], [10, 0], [1, 2]]
	l = calculateScoreForFrames(game)
	print "Strike at 10th frame: \n", "Expected: 67", "Calculated: ", calculateScoreForGame(l)
	game = [[2, 3], [1, 2], [3, 4], [6, 2], [1, 2], [2, 3], [3, 4], [5, 2], [1, 5], [1, 9]]
	l = calculateScoreForFrames(game)
	#game ended prematurely: expected score: 61
	print "Spare Ended prematurely at 10th frame: \n", "Expected: 61", "Calculated: ", calculateScoreForGame(l)
	
	#testing a Score without any strikes or spares
	game = [[1, 7], [2, 3], [1, 8]]
	l = calculateScoreForFrames(game)
	#expected: 22
	print "Score of a game without any strikes or spares: \n", "Expected: 22", "Calculated: ", calculateScoreForGame(l)
	