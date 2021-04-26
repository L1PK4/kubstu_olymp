#include <iostream>
#define ll long long
#define ull unsigned long long


void qsrt(ull *arr, ull *pos, ll low, ll high)
{
    ll i = low,
        j = high;
    ull pivot = arr[(i + j) / 2];
    ll temp;
    while (i <= j)
    {
        while (arr[i] < pivot)
            i++;
        while (arr[j] > pivot)
            j--;
        if (i <= j)
        {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            temp = pos[i];
            pos[i] = pos[j];
            pos[j] = temp;
            i++;
            j--;
        }
    }
    if (j > low)
        qsrt(arr, pos, low, j);
    if (i < high)
        qsrt(arr, pos, i, high);
}

ll binsearch(ull *arr, ll low, ll high, ull task)
{
    if (high >= low)
    {
        ll mid = low + (high - low) / 2;
        if (arr[mid] == task)
            return mid;
        if (arr[mid] > task)
            return binsearch(arr, low, mid - 1, task);
        return binsearch(arr, mid + 1, high, task);
    }
    return -1;
}


ull *arr,   
     *pos;
ull n, m;
ll temp;

using namespace std;

int main()
{
    cin >> n;
    arr = new ull[n];
    pos = new ull[n];
    for (ull i = 0; i < n; i++)
    {
        cin >> arr[i];
        pos[i] = i;
    }
    qsrt(arr, pos, 0, n - 1);
    cin >> m;
    for (ull i = 0; i < m; i++)
    {
        cin >> temp;
        ll p = binsearch(arr, 0, n, (ull) temp);
        if (p < 0){
            cout << "-1\n"; 
        } else {
            cout << pos[p] << endl;
        }
    }
    delete[] pos;
    delete[] arr;
    return 0;
}