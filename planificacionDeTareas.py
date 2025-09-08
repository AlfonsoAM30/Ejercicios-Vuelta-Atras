import heapq

def get_csf(cost_matrix, partial_solution):
    csf = 0
    for i in range(len(cost_matrix)):
        if partial_solution[i] != -1:
            csf += cost_matrix[i][partial_solution[i]]
    return csf


def get_gfc(cost_matrix, partial_solution):
    gfc = 0
    n = len(cost_matrix)
    free_row = []
    free_columns = []
    for i in list(range(len(cost_matrix))):
        if i not in partial_solution:
            free_columns.append(i)

    for i in list(range(len(cost_matrix))):
        if i == partial_solution[i]:
            free_row.append(i)

    for i in range(n):
        min_element = float('inf')
        final_min = 0
        for j in range(n):
            if i in free_row and j in free_columns:
                if cost_matrix[i][j] < min_element:
                    min_element = cost_matrix[i][j]
                    final_min = min_element
        gfc += final_min

    return gfc


def get_ffc(cost_matrix, partial_solution):
    ffc = 0
    n = len(cost_matrix)
    free_row = []
    free_columns = []
    for i in list(range(len(cost_matrix))):
        if i not in partial_solution:
            free_columns.append(i)

    for i in list(range(len(cost_matrix))):
        if i == partial_solution[i]:
            free_row.append(i)

    for i in range(n):
        min_element = float('inf')
        final_min = 0
        saved_column = 0
        saved_row = 0
        for j in range(n):
            if i in free_row and j in free_columns:
                if cost_matrix[i][j] < min_element:
                    min_element = cost_matrix[i][j]
                    final_min = min_element
                    saved_row = i
                    saved_column = j
        if final_min != 0:
            free_row.remove(saved_row)
            free_columns.remove(saved_column)




def job_assignment(cost_matrix):
    n = len(cost_matrix)
    global_upper_bound = 0
    assigned_tasks = []
    #calcular la cota superior inicial
    for i in range(n):
        min_element = float('inf')
        final_min = 0
        task_to_assign = -1
        for j in range(n):
            if j not in assigned_tasks:
                if cost_matrix[i][j] < min_element:
                    min_element = cost_matrix[i][j]
                    final_min = cost_matrix
                    task_to_assign = j
        if final_min != 0:
            assigned_tasks.append(task_to_assign)
            global_upper_bound += final_min
    print("Valor inicial de la cota superior:", global_upper_bound)
    p = []

    for i in range(n):
        partial_solution = [i] + [-1] * (n-1)
        csf = get_csf(cost_matrix, partial_solution)
        gfc = get_gfc(cost_matrix, partial_solution)
        ffc = get_ffc(cost_matrix, partial_solution)
        lower_bound = csf + gfc
        upper_bound = csf + ffc
        if lower_bound > global_upper_bound:
            continue
        else:
            temp_sol = partial_solution.copy()
            partial_tuple = (lower_bound, temp_sol)
            heapq.heappush(p, partial_tuple)
            if upper_bound < global_upper_bound:
                global_upper_bound = upper_bound
    while len(p) != 0:
        partial_tuple = heapq.heappop(p)
        partial_solution = partial_tuple[1]
        if partial_solution[-1] != -1:
            final_sum = get_csf(cost_matrix, partial_solution)
            return final_sum, partial_solution
        else:
            extended = []
            for i in list(range(n)):
                if i not in partial_solution:
                    extended.append(i)
        i = n - len(extended)
        for j in extended:
            partial_solution[i] = j
            csf = get_csf(cost_matrix, partial_solution)
            gfc = get_gfc(cost_matrix, partial_solution)
            ffc = get_ffc(cost_matrix, partial_solution)
            lower_bound = csf + gfc
            upper_bound = csf + ffc
            if lower_bound > global_upper_bound:
                continue
            else:
                temp_sol = partial_solution.copy()
                partial_tuple = (lower_bound, temp_sol)
                heapq.heappush(p, partial_tuple)
                if upper_bound < global_upper_bound:
                    global_upper_bound = upper_bound


if __name__ == '__main__':
    cost_matrix = [
        [11, 12, 18, 40],
        [14, 15, 13, 22],
        [11, 17, 19, 23],
        [17, 14, 20, 28]
    ]
    job_assignment(cost_matrix)
