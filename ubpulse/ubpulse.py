import serial
import time
import csv

# 시리얼 포트 설정 (포트 이름과 보드레이트를 기기에 맞게 설정)
serial_port = 'COM3'  # Windows에서는 'COM3' 같은 형식으로 사용
baud_rate = 9600  # 기기 매뉴얼에 맞는 보드레이트

# 시리얼 포트 열기
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# 데이터 저장할 파일 열기
csvFileName = './ubpulse/ubpulse_data.csv'

try:
    with open(csvFileName, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['PPG', 'HI', 'HR', 'HR_A', 'PI', 'PI_A'])

    PPG = 0
    HI = 0
    HR = 0
    HR_A = 0
    PI1 = 0
    PI2 = 0
    PI = 0
    PI_A1 = 0
    PI_A2 = 0
    PI_A = 0
    print("데이터 수집을 시작합니다.")
    while True:
        if ser.in_waiting > 0:
            # 시리얼로부터 데이터 읽기
            data = ser.read(ser.in_waiting)  # 가용한 모든 데이터를 읽기
            
            # print(data)
            # 10진수 변환: 각 바이트를 10진수로 변환
            decimal_data = [str(byte) for byte in data]  # 각 바이트를 10진수로 변환하여 문자열 리스트로 저장
            
            # 10진수 데이터를 출력 및 파일에 저장
            decimal_string = ' '.join(decimal_data)  # 각 10진수 값을 공백으로 구분
            packit_list = decimal_string.split('255 254 ')
            print("수신된 데이터 개수: " , str(len(packit_list)-1))
            for packit in packit_list[1:]:
                # print(packit)
                packit_data = packit.split(' ')
                PPG = (int(packit_data[5])%16)*256+(int(packit_data[6])%256)
                HI = (int(packit_data[3])%8)*256+(int(packit_data[0])%256)
                HR = int(packit_data[4]) if int(packit_data[2])==2 else HR
                PI1 = int(packit_data[4])%16 if int(packit_data[2])==3 else PI1
                PI2 = int(packit_data[4])%256 if int(packit_data[2])==4 else PI2
                PI = (PI1*256+PI2)/100 if int(packit_data[2])==4 else PI
                HR_A = int(packit_data[4]) if int(packit_data[2])==5 else HR_A
                PI_A1 = int(packit_data[4])%16 if int(packit_data[2])==6 else PI_A1
                PI_A2 = int(packit_data[4])%256 if int(packit_data[2])==7 else PI_A2
                PI_A = (PI_A1*256+PI_A2)/100 if int(packit_data[2])==7 else PI_A

                with open(csvFileName, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([str(PPG), str(HI), str(HR), str(HR_A), str(PI), str(PI_A)])
            
            # 필요에 따라 데이터 처리 추가 가능

        # 데이터 수집 주기 설정 (0.5초 간격으로 데이터 수집)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("데이터 수집을 중단합니다.")

finally:
    # 시리얼 포트 닫기
    ser.close()
