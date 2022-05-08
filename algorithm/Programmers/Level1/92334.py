def solution(id_list, report, k):
    report = list(set(report))
    id_list_len = len(id_list)
    report_dict: 'dict[str, set]' = {id_list[_]: set() for _ in range(id_list_len)}
    reported_count_dict: 'dict[str, num]' = {id_list[_]: 0 for _ in range(id_list_len)}
    result_count = [0] * id_list_len

    for r in report:
        reporter, reportee = r.split()
        report_dict[reporter].add(reportee)

    for i in range(id_list_len):
        reportee_list = report_dict[id_list[i]]
        for rpt in reportee_list:
            reported_count_dict[rpt] += 1

    for i in range(id_list_len):
        report_dict[id_list[i]]
        while report_dict[id_list[i]]:
            rpt = report_dict[id_list[i]].pop()
            if reported_count_dict[rpt] >= k:
                result_count[i] += 1

    return result_count
