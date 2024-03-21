# Python Scheduler

A Python script that allows to schedule the execution of asynchronous activities with different frequencies.

A port of my [Schedule](https://github.com/fabioscagliola/Schedule) .NET console application to Python.

Sample output:

```
2024-03-21 08:09:35 — Python Scheduler began.
2024-03-21 08:09:35 — Press CTRL + C to quit.
2024-03-21 08:09:35 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Executing activity "Numb"..
2024-03-21 08:09:35 — [2aef44dd-1aab-44e9-831f-f523fd6048df] Executing activity "Foul"..
2024-03-21 08:09:35 — [73f38692-960d-4fd8-b1d8-8e0d1e2bd71f] Executing activity "Hash"..
2024-03-21 08:09:37 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Fibonacci number at position 9 is 34
2024-03-21 08:09:38 — [73f38692-960d-4fd8-b1d8-8e0d1e2bd71f] The MD5 hash of "Lisan al-Gaib" is 3396da2c8897f8b6333c2319a17f0481
2024-03-21 08:09:39 — [2aef44dd-1aab-44e9-831f-f523fd6048df] Something went wrong while attempting to execute activity Foul:
2024-03-21 08:09:39 — [2aef44dd-1aab-44e9-831f-f523fd6048df]   May your knife chip and shatter
2024-03-21 08:09:45 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Executing activity "Numb"..
2024-03-21 08:09:47 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Fibonacci number at position 9 is 34
2024-03-21 08:09:55 — [73f38692-960d-4fd8-b1d8-8e0d1e2bd71f] Executing activity "Hash"..
2024-03-21 08:09:55 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Executing activity "Numb"..
2024-03-21 08:09:57 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Fibonacci number at position 9 is 34
2024-03-21 08:09:58 — [73f38692-960d-4fd8-b1d8-8e0d1e2bd71f] The MD5 hash of "Lisan al-Gaib" is 3396da2c8897f8b6333c2319a17f0481
2024-03-21 08:10:05 — [2aef44dd-1aab-44e9-831f-f523fd6048df] Executing activity "Foul"..
2024-03-21 08:10:05 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Executing activity "Numb"..
2024-03-21 08:10:07 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Fibonacci number at position 9 is 34
2024-03-21 08:10:09 — [2aef44dd-1aab-44e9-831f-f523fd6048df] Something went wrong while attempting to execute activity Foul:
2024-03-21 08:10:09 — [2aef44dd-1aab-44e9-831f-f523fd6048df]   May your knife chip and shatter
2024-03-21 08:10:15 — [73f38692-960d-4fd8-b1d8-8e0d1e2bd71f] Executing activity "Hash"..
2024-03-21 08:10:15 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Executing activity "Numb"..
2024-03-21 08:10:17 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Fibonacci number at position 9 is 34
2024-03-21 08:10:18 — [73f38692-960d-4fd8-b1d8-8e0d1e2bd71f] The MD5 hash of "Lisan al-Gaib" is 3396da2c8897f8b6333c2319a17f0481
2024-03-21 08:10:25 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Executing activity "Numb"..
2024-03-21 08:10:27 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Fibonacci number at position 9 is 34
2024-03-21 08:10:35 — [2aef44dd-1aab-44e9-831f-f523fd6048df] Executing activity "Foul"..
2024-03-21 08:10:35 — [73f38692-960d-4fd8-b1d8-8e0d1e2bd71f] Executing activity "Hash"..
2024-03-21 08:10:35 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Executing activity "Numb"..
2024-03-21 08:10:37 — [edab6ffe-b0cf-4360-bdf3-367cd8e28ae5] Fibonacci number at position 9 is 34
2024-03-21 08:10:38 — [73f38692-960d-4fd8-b1d8-8e0d1e2bd71f] The MD5 hash of "Lisan al-Gaib" is 3396da2c8897f8b6333c2319a17f0481
2024-03-21 08:10:39 — [2aef44dd-1aab-44e9-831f-f523fd6048df] Something went wrong while attempting to execute activity Foul:
2024-03-21 08:10:39 — [2aef44dd-1aab-44e9-831f-f523fd6048df]   May your knife chip and shatter
2024-03-21 08:10:40 — Python Scheduler ended.
```

