
import cv2

carmera = cv2.VideoCapture(0) #웹캠과 연결

if not carmera.isOpened(): #웹캠이 감지되지 않으면
	print("There is no carmera")
	exit()
else:
	while carmera.isOpened():
		status, frame = carmera.read() #웹캠에서 촬영되는 영상을 읽어냄
		frame = cv2.flip(frame,1)# 좌우대칭을 마춰줌
		if status:
			cv2.imshow("test", frame) # 읽어낸 영상을 test라는 창에 출력
		if cv2.waitKey(1) & 0xFF == ord('q'): #q를 입력할씨 출력 중단.
			break

carmera.release() #웹캠과 연결 해제
cv2.destroyAllWindows()
