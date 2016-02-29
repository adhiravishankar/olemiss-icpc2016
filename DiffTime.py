
while True:
    a = [str(i) for i in input().split()]
    months = []
    if a[0] == 0:
        break
    numSecs = int(a[0])
    numMins = int(a[1])
    numHours = int(a[2])
    numMonths = int(a[3])
    for month in range(1, numMonths):
        months.append(int(a[month]) + 3)
    startDateTime = a[4 + numMonths].split('-')
    endDateTime = a[5 + numMonths].split('-')

    startDate = [int(i) for i in startDateTime[0].split('/')]
    startTime = [int(i) for i in startDateTime[0].split(':')]
    endDate = [int(i) for i in endDateTime[0].split('/')]
    endTime = [int(i) for i in endDateTime[0].split(':')]

    diffDays = 0

    while startDate != endDate:
        if startDate[2] == endDate[2]:
            if startDate[0] == endDate[0]:
                diffDays += endDate[1] - startDate[1]
            else:
                if startDate[0] / 12 == 0:
                    endDate[1] += months[startDate[0] - 1]
                    startDate[0] -= 1
                else:
                    endDate[1] += months[(startDate[0]  % 12) - 1]
                    startDate[0] -= 1
        else:
            if endDate[2] - startDate[2] >= 1:
                endDate[1] += endDate[2] - startDate[2] * sum(months)
            else:
                endDate[0] += numMonths
                endDate[2] -= 1


    diffDaysInHours = diffDays * numHours

    diffHoursInMins = diffDaysInHours + (endTime[0] - endTime[0]) * numMins
    diffMinsInSecs = diffHoursInMins + (endTime[1] - endTime[1]) * numSecs
    diff = diffMinsInSecs + endTime[2] - endTime[2];

    print(diff)
