class ReservationSystem:
    all_reservations = []  # 모든 지점의 예약을 저장할 클래스 변수

    def __init__(self, location):
        """
        레스토랑 지점의 이름을 초기화하고 예약 리스트를 관리합니다.
        """
        self.location = location
        self.reservations = []  # 해당 지점의 예약 리스트

    def add_reservation(self, customer_name, reservation_time, num_people):
        """
        새로운 예약을 추가합니다.
        :param customer_name: 예약자의 이름
        :param reservation_time: 예약 일시
        :param num_people: 인원 수
        """
        if not customer_name or not reservation_time or num_people <= 0:
            print("예약 정보를 올바르게 입력해 주세요.")
            return
        
        reservation = {
            'customer_name': customer_name,
            'reservation_time': reservation_time,
            'num_people': num_people
        }
        self.reservations.append(reservation)
        ReservationSystem.all_reservations.append(reservation)  # 모든 예약 리스트에 추가
        print(f"{self.location} 지점에 예약이 추가되었습니다: {reservation}")

    def cancel_reservation(self, customer_name, reservation_time):
        """
        지정된 예약을 취소합니다.
        :param customer_name: 예약자의 이름
        :param reservation_time: 예약 일시
        """
        if not customer_name or not reservation_time:
            print("예약 취소 정보를 올바르게 입력해 주세요.")
            return

        initial_count = len(self.reservations)
        self.reservations = [
            res for res in self.reservations
            if not (res['customer_name'] == customer_name and res['reservation_time'] == reservation_time)
        ]
        ReservationSystem.all_reservations = [
            res for res in ReservationSystem.all_reservations
            if not (res['customer_name'] == customer_name and res['reservation_time'] == reservation_time)
        ]

        if len(self.reservations) < initial_count:
            print(f"{self.location} 지점의 예약이 취소되었습니다.")
        else:
            print("취소할 예약을 찾을 수 없습니다.")

    def list_reservations(self):
        """
        현재 지점의 모든 예약 상태를 출력합니다.
        """
        print(f"{self.location} 지점의 예약 현황:")
        if not self.reservations:
            print("현재 예약이 없습니다.")
        for reservation in self.reservations:
            print(f"예약자: {reservation['customer_name']}, 일시: {reservation['reservation_time']}, 인원: {reservation['num_people']}")

    @classmethod
    def sum_reservations(cls):
        """
        모든 지점의 예약 수를 합산합니다.
        """
        total_reservations = len(cls.all_reservations)
        print(f"전체 지점의 예약 수: {total_reservations}")
        return total_reservations


# 사용 예시
if __name__ == "__main__":
    restaurant1 = ReservationSystem("홍대점")
    restaurant2 = ReservationSystem("강남점")

    restaurant1.add_reservation("홍길동", "2024-05-20 19:00", 4)
    restaurant2.add_reservation("김철수", "2024-05-21 20:00", 2)
    
    restaurant1.list_reservations()
    restaurant2.list_reservations()
    
    restaurant1.cancel_reservation("홍길동", "2024-05-20 19:00")
    restaurant1.list_reservations()
    
    ReservationSystem.sum_reservations()

    restaurant2.list_reservations()

    print("\n")
    total_reservations = ReservationSystem.sum_reservations([restaurant1, restaurant2])