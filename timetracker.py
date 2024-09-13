from datetime import datetime

class TimeTracker:
    def __init__(self):
        self.start_time = None
        self.stop_time = None
    # 공부 시작 시간
    def start(self):
        self.start_time = datetime.now()
        print(f'활동 시작 시간 : {self.start_time}')
    # 공부 끝난 시간
    def stop(self):
        self.stop_time = datetime.now()
        print(f'활동 종료 시간 : {self.stop_time}')
    # 총 소요 시간
    def get_elapsed_time(self):
        elapsed_time = self.stop_time - self.start_time
        return elapsed_time.total_seconds() / 60 # 분 단위로 반환을 위해 60으로 나눠줌




# 사용 예시
if __name__ == "__main__":
    tracker = TimeTracker()
    tracker.start()

    # # 여기서 실제로 시간을 지연시키려면 time.sleep()을 사용할 수 있지만, 코드 실행을 바로 확인하기 위해 주석 처리함
    import time
    time.sleep(61)  # 61초 대기

    tracker.stop()
    print(f"공부한 시간: {tracker.get_elapsed_time()} 분

