#include <stdio.h>
#include <stdlib.h>

#define MAX_JOBS 100

// Structure to represent a Job
struct Job {
    int jobId;
    int burstTime;
    int priority;
};

// Function to perform First Come First Serve (FCFS) scheduling
void fcfsScheduling(struct Job jobs[], int n) {
    printf("\n--- First Come First Serve Scheduling ---\n");
    int waitingTime = 0, turnaroundTime = 0, totalWaitingTime = 0, totalTurnaroundTime = 0;
    
    for (int i = 0; i < n; i++) {
        turnaroundTime = waitingTime + jobs[i].burstTime;
        totalWaitingTime += waitingTime;
        totalTurnaroundTime += turnaroundTime;
        printf("Job %d -> Waiting Time: %d, Turnaround Time: %d\n", jobs[i].jobId, waitingTime, turnaroundTime);
        waitingTime += jobs[i].burstTime;
    }
    
    printf("Average Waiting Time: %.2f\n", (float)totalWaitingTime / n);
    printf("Average Turnaround Time: %.2f\n", (float)totalTurnaroundTime / n);
}

// Function to perform Priority Scheduling
void priorityScheduling(struct Job jobs[], int n) {
    printf("\n--- Priority Scheduling ---\n");
    
    // Sorting jobs by priority (ascending order)
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (jobs[i].priority > jobs[j].priority) {
                struct Job temp = jobs[i];
                jobs[i] = jobs[j];
                jobs[j] = temp;
            }
        }
    }

    // Applying FCFS on sorted jobs
    fcfsScheduling(jobs, n);
}

int main() {
    struct Job jobs[MAX_JOBS];
    int n, choice;

    printf("Enter the number of jobs: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        printf("Enter details for Job %d:\n", i + 1);
        jobs[i].jobId = i + 1;
        printf("Burst Time: ");
        scanf("%d", &jobs[i].burstTime);
        printf("Priority (lower value means higher priority): ");
        scanf("%d", &jobs[i].priority);
    }

    printf("\nChoose Scheduling Policy:\n");
    printf("1. First Come First Serve (FCFS)\n");
    printf("2. Priority Scheduling\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            fcfsScheduling(jobs, n);
            break;
        case 2:
            priorityScheduling(jobs, n);
            break;
        default:
            printf("Invalid choice! Please choose 1 or 2.\n");
            break;
    }

    return 0;
}
