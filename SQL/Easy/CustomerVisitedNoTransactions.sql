-- Problem: Customer Who Visited but Did Not Make Any Transactions (LeetCode #1581)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions

-- Select customer_id from the visits table, as well as counts the numbers of visit ids (important that it is grouped by customer id later)
SELECT
    v.customer_id,
    COUNT(v.visit_id) AS count_no_trans
-- FROM the Visits table as v
FROM
    Visits v
-- Joins Visits with Transactions, keeping all rows from Visits and adding NULL for unmatched rows:
LEFT JOIN
    Transactions t
-- on matching visit_ids
ON
    v.visit_id = t.visit_id
-- Filters rows to only include those where it is null in the transaction visit_id
WHERE
    t.visit_id IS NULL
GROUP BY
    v.customer_id
ORDER BY
    v.customer_id;