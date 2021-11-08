Tests to be performed are Blackbox input partitioning, output partitioning, and boundry testing
Boundry testing is implemented on all input partitioning tests by selecting values at or just above the boundry, for each partition.

Lines 1-23 are setup code creating a user and a test product, and another product to check for title validity against

#Title input partitioning
Lines 24-31 are test on title being alphanumeric + no invalid spaces + less than 80 chars + Title not already in use #This case also satisfies input partition for each variable where the expected output is true, so those will be ommited from this point on
Lines 32-39 are test on title being alphanumeric + no invalid spaces + greater than 80 chars + Title not already in use
Lines 40-47 are test on title being alphanumeric + invalid spaces + less than 80 chars + Title not already in use
Lines 48-55 are test on title being not alphanumeric + no invalid spaces + less than 80 chars + Title not already in use
Lines 56-63 are test on title being alphanumeric + no invalid spaces + less than 80 chars + Title already in use

#Description input partitioning
Lines 64-71 are test on description being greater than 20 chars + less than 2001 characters + not longer than title
Lines 72-79 are test on description being greater than 20 chars + greater than 2001 characters + longer than title
Lines 80-87 are test on description being less than 20 chars + less than 2001 characters + longer than title

#Price input partitioning
Lines 88-95 are test on price being increased + being atleast 10 + more than 10,000
Lines 96-103 are test on price being increased + being less than 10 + no more than 10,000
Lines 104-111 are test on price being descreased + being atleast 10 + no more than 10,000

#Email input partitioning
Lines 112-115 are test on email not existing

#Output paritioning
Lines 116-123 are testing for valid ouput
Lines 124-131 are testing for invalid output