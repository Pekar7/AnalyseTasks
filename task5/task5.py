import numpy as np
import json

def isString(value) -> bool:
  return isinstance(value, str)

def getRankingLength(ranking: list) -> int:
  rankingLength = 0
  for rankingGroup in ranking:
    if isString(rankingGroup):
      rankingLength += 1
    else:
      rankingLength += len(rankingGroup)
  return rankingLength

def getRelationMatrix(ranking: list) -> list:
  ranksAmount = getRankingLength(ranking)
  relationMatrix = np.array([[0 for _ in range(ranksAmount)] for _ in range(ranksAmount)])
  for rankGroupInd, rankGroup in enumerate(ranking):
    rankList = [0 for _ in range(ranksAmount)]
    for remainingGroup in ranking[rankGroupInd:]:
      if isString(remainingGroup):
        rankList[int(remainingGroup) - 1] = 1
      else:
        for remainingRank in remainingGroup:
          rankList[int(remainingRank) - 1] = 1
    if isString(rankGroup):
      relationMatrix[:][int(rankGroup) - 1] = rankList
    else:
      for rank in rankGroup:
        relationMatrix[:][int(rank) - 1] = rankList
  return relationMatrix


def task(rankingL: str, rankingR: str) -> list:
  rankingL = json.loads(rankingL)
  rankingR = json.loads(rankingR)
  relationMatrixL = getRelationMatrix(rankingL)
  relationMatrixR = getRelationMatrix(rankingR)

  y = relationMatrixL * relationMatrixR
  yTransposed = relationMatrixL.T * relationMatrixR.T
  core = y | yTransposed
  conflicts = np.where(core == 0)
  conflictPairs = [[str(conflict[0] + 1), str(conflict[1] + 1)] for conflict in conflicts if conflict[0] < conflict[1]]

  return json.dumps(conflictPairs)
