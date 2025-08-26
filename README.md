# project3
11124231蔡雅婷、11124134翁語鮮

# 思路與算法
Ⅰ、桶排序

① 初始化桶和頻率陣列：建立「字串長度+1」的桶 bucket，索引 i 表示頻率為 i 的字元列表；同時建立長度為 max 的頻率陣列 count，用於記錄每個字元的出現次數。

② 統計字元頻率：透過 ord(char) 取得字元的 ASCII 碼，作為頻率陣列的索引。

③ 將字元按照頻率放入桶中：遍歷頻率陣列，將每個字元以其頻率作為索引放入桶中。

④ 返回桶陣列：返回桶陣列，其中每個桶包含對應頻率的字元列表。

# 算法流程

1.設定固定數量的空桶。

2.將數據放入對應的桶中。

3.對每個非空桶進行排序。

4.合併所有不為空的桶資料，生成排序後的結果。

# 選擇排序 (Selection Sort)

原理：

1.遍歷數組：從索引 0 到 n-1（n 為數組長度）。

2.每輪確定最小值：假設當前索引 i 為最小值索引 min_index。從 i+1 到 n-1 遍歷，若找到更小元素，則更新 min_index。

3.交換元素：若 min_index ≠ i，則交換 arr[i] 與 arr[min_index]。
<img width="606" height="267" alt="螢幕擷取畫面 2025-08-26 164703" src="https://github.com/user-attachments/assets/f0847c36-5e33-43b7-8f44-c9d65fe30f83" />
<img width="331" height="30" alt="螢幕擷取畫面 2025-08-26 164853" src="https://github.com/user-attachments/assets/b009df07-bf30-454d-84c2-78ac68385565" />


# 冒泡排序 (Bubble Sort)

原理：

1.初始化：設數組長度為 n。

2.外層循環：遍歷 i 從 0 到 n-1（共 n 輪）。

3.內層循環：對於每輪 i，遍歷 j 從 0 到 n-i-2。

4.比較與交換：若 arr[j] > arr[j+1]，則交換兩者。

5.結束條件：重複步驟 2-4，直到所有輪次完成。

<img width="561" height="207" alt="螢幕擷取畫面 2025-08-26 164903" src="https://github.com/user-attachments/assets/2c909c31-26e3-4375-8e13-4df3034d53cd" />

<img width="302" height="23" alt="螢幕擷取畫面 2025-08-26 164911" src="https://github.com/user-attachments/assets/93e413ee-b39b-4628-a35f-072ec7159117" />


# 插入排序 (Insertion Sort)

原理：

1.遍歷未排序元素：從索引 1 到 n-1。

2.保存當前元素：將 arr[i] 存入 current。

3.元素後移：從已排序部分的末尾（索引 j = i-1）向前掃描，將比 current 大的元素後移。直到找到第一個不大于 current 的位置或掃描完所有元素。

4.插入元素：將 current 放入 j+1 位置。

<img width="564" height="287" alt="螢幕擷取畫面 2025-08-26 165251" src="https://github.com/user-attachments/assets/927f1279-517e-425f-a80f-5a874c10b49a" />

<img width="311" height="26" alt="螢幕擷取畫面 2025-08-26 165259" src="https://github.com/user-attachments/assets/b7855caa-394d-4d63-a9db-7b982f6268e4" />

# 計數排序 (Counting Sort)

原理：

1.初始化：設數組長度為 n，元素最大值為 r。創建長度為 r+1 的計數數組 count，初始值全為 0。

2.統計元素頻率：遍歷原數組 arr，對每個元素 x，將 count[x] 加 1。

3.重構有序數組：初始化索引 index = 0。遍歷計數數組 count，索引 v 從 0 到 r，若 count[v] > 0，則將 v 填入原數組 arr[index]，並將 index 加 1。重複此步驟直到 count[v] 為 0。

4.結束條件：當計數數組遍歷完成時，排序結束。

<img width="655" height="314" alt="螢幕擷取畫面 2025-08-26 165308" src="https://github.com/user-attachments/assets/332f4dc6-bb74-4f73-92b4-bef8c8f3fefc" />

<img width="335" height="23" alt="螢幕擷取畫面 2025-08-26 165313" src="https://github.com/user-attachments/assets/7885830c-df9c-493e-bdd8-e10e7bf66650" />

# 歸併排序 (Merge Sort)

原理：

Ⅰ、遞歸分解列表

1.終止條件：若鏈表為空或只有一個節點，直接返回頭節點。

2.快慢指針找中點：初始化 slow 和 fast 指針，slow 指向頭節點，fast 指向頭節點的下一個節點。fast 每次移動兩步，slow 每次移動一步。當 fast 到達末尾時，slow 恰好指向鏈表的中間節點。

3.分割鏈表：將鏈表從中點斷開，head2 指向 slow.next（後半部分的頭節點）。將 slow.next 置為 None，切斷前半部分與後半部分的連接。

4.遞歸排序子鏈表：對前半部分（head）和後半部分（head2）分別遞歸調用 mergesort 函數。

Ⅱ、合併兩個有序列表

1.創建虛擬頭節點：創建一個值為 -1 的虛擬節點 zero，用于簡化邊界處理。使用 current 指針指向 zero，用于構建合併後的鏈表。

2.比較並合併節點：遍歷兩個子鏈表 head1 和 head2，比較當前節點的值：若 head1.val <= head2.val，將 head1 接入合併鏈表，並移動 head1 指針。否則，將 head2 接入合併鏈表，並移動 head2 指針。每次接入節點後，移動 current 指針到新接入的節點。

3.處理剩余節點：當其中一個子鏈表遍歷完後，將另一個子鏈表的剩余部分直接接入合併鏈表的末尾。

4.返回合併後的鏈表：虛擬節點 zero 的下一個節點即為合併後的有序鏈表的頭節點。

<img width="805" height="836" alt="3" src="https://github.com/user-attachments/assets/1a0871b2-58e5-4427-9e5c-8214736cb42b" />

<img width="170" height="26" alt="螢幕擷取畫面 2025-08-26 170621" src="https://github.com/user-attachments/assets/e7236069-54d1-4c64-b8e3-4d4dfaa4413a" />
