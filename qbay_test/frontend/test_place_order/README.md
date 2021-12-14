Tests to be performed are Blackbox input partitioning, output partitioning

Lines 1-28 are setup code creating a user and a test product, and another user to act as a buyer
Aside from the first case in Buyer input partitioning, the valid partition for the other cases is omitted, as the first one satisfies the requirement for the rest.

#Buyer input partitioning
Lines 29-33 Partitioning on a valid buyer
Lines 34-38 Partitioning on when Buyer doesnt exist
Lines 39-43 Partitioning when Buyer is seller

#Seller input partitioning
Lines 44-48 Partitioning when Seller doesnt exist
#Seller is buyer omitted as it is covered by Buyer is seller

#Price/Balance input partitioning
Lines 49-53 Partitioning on when price is more than balance

#Product input partitioning
Lines 54-58 Partitioning on when product doesnt exist

#Output paritioning
Lines 59-63 Valid output
Lines 64-68 Invalid output