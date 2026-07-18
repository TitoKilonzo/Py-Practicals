       IDENTIFICATION DIVISION.
       PROGRAM-ID. PATIENT.
       AUTHOR. KILONZO.
       DATE-WRITTEN. 2026-07-02.

       DATA DIVISION.
       WORKING-STORAGE SECTION.

       01  WS-PATIENT-ID            PIC 9(06).

       01  WS-PATIENT-NAME.
           05  WS-FIRST-NAME        PIC X(20).
           05  WS-SURNAME           PIC X(25).

       01  WS-AGE                   PIC 9(03).

       01  WS-WARD-CODE             PIC X(03).

       01  WS-DIAGNOSIS-CODE        PIC X(10).

       01  WS-TEST-RESULTS.
           05  WS-TEST-1            PIC 9(03)V9(02).
           05  WS-TEST-2            PIC 9(03)V9(02).
           05  WS-TEST-3            PIC 9(03)V9(02).

       01  WS-ATTENDING-DOCTOR      PIC X(30).

       01  WS-TEST-DISPLAY          PIC ZZ9.99.

       01  WS-SEPARATOR             PIC X(50) VALUE ALL "-".

       PROCEDURE DIVISION.

       MAIN-LOGIC.
           STOP RUN.
