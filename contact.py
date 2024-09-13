# 주소록 클래스 

class Contact:
    # 인스턴스 초기화 메서드
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    # 스트링 메서드
    def __str__(self):
        return f'이름: {self.name} \n전화번호: {self.phone} \n이메일: {self.email}'




# 사용 예시
if __name__ == "__main__":
    # 연락처 정보 생성
    friend = Contact("Jane Doe", "010-1234-5678", "jane@example.com")
    # 연락처 정보 출력
    print(friend)

# 1번 비해서 상당히 무난했던 문제. __init__ 메소드에서 "이름,전화번호,이메일"을 인스턴스로 받아줘야 했음 
