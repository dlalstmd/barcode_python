def sort(arr): #sort 함수 정의
    for i in range(len(arr) - 1) : #(자료 수)-1회 반복 설정
        min_idx = i #min_idx 변수 설정
        for j in range(i + 1 , len(arr)): #min_idx 이후의 원소들을 비교
            if arr[j] < arr[min_idx] : #최솟값을 업데이트
                min_idx = j # i > j일 경우 j가 최솟값
            
        swap(arr, i, min_idx) #swap 함수 

def swap(arr, i, j) :
    arr[i], arr[j] = arr[j], arr[i] #i와j에 해당하는 원소 위치 재정렬

    ...

arr = [3,5,2,1,4,8,10,7,6,9]
sort(arr)
print(arr)
