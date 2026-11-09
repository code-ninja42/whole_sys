# Heap

## Definition

A **Heap** is a special tree-based data structure where the parent node is either greater than or smaller than its child nodes. In Python, the `heapq` module implements a **Min Heap**.

---

## Why do we use it?

* To find the smallest or largest element quickly.
* To implement priority queues.
* To perform heap sort.
* To optimize scheduling algorithms.

---

## Key Points

* Heap is a complete binary tree.
* Python's `heapq` provides a Min Heap.
* Smallest element is always at the root.
* Stored internally as a list.

---

## Syntax

```python id="v4xqg9"
import heapq

heap = []
```

---

## Parameters

| Function        | Description                   |
| --------------- | ----------------------------- |
| `heapify()`     | Converts a list into a heap   |
| `heappush()`    | Inserts an element            |
| `heappop()`     | Removes the smallest element  |
| `heappushpop()` | Pushes then pops an element   |
| `heapreplace()` | Replaces the smallest element |

---

## Return Value

Returns the smallest element or a heap depending on the function used.

---

## Internal Working

A heap is stored as a list. Parent and child relationships are maintained automatically to satisfy the heap property.

---

## Rules

* Import the `heapq` module.
* Python uses a Min Heap by default.
* Root always contains the smallest value.
* Heap is stored as a complete binary tree.

---

## Types (if applicable)

### 1. Min Heap

Parent is smaller than its children.

### 2. Max Heap

Parent is larger than its children.

---

## Advantages

* Fast insertion.
* Fast deletion.
* Efficient priority queue.
* Finds minimum quickly.

---

## Disadvantages

* Searching arbitrary elements is slow.
* Python does not provide a built-in Max Heap.
* Complex compared to lists.

---

## Time Complexity

| Operation    | Complexity   |
| ------------ | ------------ |
| Insert       | **O(log n)** |
| Delete       | **O(log n)** |
| Peek Minimum | **O(1)**     |
| Heapify      | **O(n)**     |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python id="p6n6zm"
import heapq

heap = [5, 3, 8, 1]
heapq.heapify(heap)

print(heap)
```

### Output

```text id="wfqgq4"
[1, 3, 8, 5]
```

### Explanation

Converts a list into a Min Heap.

---

## Example 2 (Intermediate)

### Code

```python id="0kcjwn"
import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 5)

print(heap)
```

### Output

```text id="kmnnt7"
[5, 10]
```

### Explanation

Inserts elements while maintaining heap order.

---

## Example 3 (Interview)

### Code

```python id="m69jrh"
import heapq

heap = [5, 2, 8]
heapq.heapify(heap)

print(heapq.heappop(heap))
```

### Output

```text id="uvgxzv"
2
```

### Explanation

Removes and returns the smallest element.

---

## Example 4 (Real-world)

### Code

```python id="0sdcx7"
import heapq

tasks = [4, 2, 6, 1]

heapq.heapify(tasks)

print(heapq.heappop(tasks))
```

### Output

```text id="vmeplv"
1
```

### Explanation

Executes the highest-priority (smallest value) task first.

---

## Common Errors

| Error      | Reason                     | Solution                  |
| ---------- | -------------------------- | ------------------------- |
| NameError  | `heapq` not imported       | Use `import heapq`        |
| IndexError | Popping from an empty heap | Check heap before popping |

---

## Common Mistakes

* Forgetting to call `heapify()`.
* Assuming Python provides a Max Heap by default.
* Popping from an empty heap.

---

## Difference Table

| Min Heap          | Max Heap           |
| ----------------- | ------------------ |
| Smallest at root  | Largest at root    |
| Python default    | Implement manually |
| Parent ≤ Children | Parent ≥ Children  |

---

## Interview Questions

**Q1. What is a heap?**

A complete binary tree that satisfies the heap property.

**Q2. Which module is used for heaps in Python?**

`heapq`

**Q3. Does Python provide a Min Heap or Max Heap?**

Min Heap.

---

## MCQs

**1. Which module is used to implement heaps in Python?**

A. `math`

B. `heapq` ✅

C. `queue`

D. `collections`

---

**2. In a Min Heap, the root contains**

A. Largest element

B. Smallest element ✅

C. Middle element

D. Last element

---

**3. Which function converts a list into a heap?**

A. `sort()`

B. `heapify()` ✅

C. `push()`

D. `build()`

---

## Practice Questions

1. What is a heap?
2. Explain Min Heap and Max Heap.
3. Write a program using `heapify()`.
4. Insert an element using `heappush()`.
5. Remove the smallest element using `heappop()`.

---

## Real-world Applications

* Priority queues
* CPU scheduling
* Task scheduling
* Dijkstra's algorithm
* Heap sort

---

## Notes

**Remember:** Python's `heapq` implements a **Min Heap**.

**Shortcut:**

* `heapify()` → Create heap
* `heappush()` → Insert
* `heappop()` → Remove minimum

**Interview Tip:** Root always contains the smallest element in Python.

**Exam Tip:** Learn `heapify()`, `heappush()`, and `heappop()`.

---

## Summary

* A heap is a complete binary tree.
* Python uses the `heapq` module.
* Default implementation is a Min Heap.
* Used for priority queues and efficient retrieval of the smallest element.

---

## Keywords

Heap, Min Heap, Max Heap, heapq, heapify(), heappush(), heappop(), Priority Queue

---

## Related Topics

* Tree
* Priority Queue
* List
* Sorting
* Data Structures
