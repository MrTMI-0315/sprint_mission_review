class VoteSystem:
    def __init__(self):
        self.candidate = {}
    def vote(self, name):
        if name in self.candidate:
            print(f'{name}에게 투표하였습니다.')
            self.candidate[name] += 1
        else:
            print(f'{name}은 존재하지 않는 후보입니다.')
    # 투표수 출력
    def get_results(self):
        if not self.candidate: # 실행 안 돼서 계속 헷갈렸던 부분 ; '명단'에 없으면 집계할 수 없음.
            print('등록된 후보가 없습니다')
        else:
            for name, vote in self.candidate.items():
                print(f'{name} : {vote}표')





# 사용 예시
if __name__ == "__main__":
    voting_system = VoteSystem()
    voting_system.add_candidate("Alice")
    voting_system.add_candidate("Bob")
    voting_system.add_candidate("Charlie")

    voting_system.vote("Alice")
    voting_system.vote("Alice")
    voting_system.vote("Bob")

    voting_system.get_results()

# add_candidate() 함수에서 공을 좀 많이 들여야 했던 문제. 
