# The Recaman Sequence

## Introduction
    This project aims to find an efficient algorithm for generating elements of the
     Recaman Sequence. My hope is that some of the techniques used in this project
      will be applicable to other problems in the future.

## The Recaman Sequence:

    Source: https://oeis.org/A005132

    Created by Bernardo Recaman, the sequence is defined as follows:

    > a(0) = 0.
    >
    > Where n is an integer and n > 0,
    >
    >   if n is positive and not already in the sequence
    >        a(n) = a(n - 1) - n.
    >    
    >    otherwise,
    >        a(n) = a(n - 1) + n.

    Informally, go backwards if you can, otherwise go forward.

    It is, by definition, a surjection on the natural numbers.
    It remains to be proven whether the sequence is an injection on the natural numbers.

## Complexity:

    Generating numbers for the sequence is easy. The magnitude of each "jump" always 
    increases by 1, and can be determined trivially. However, every time a new member
    is generated, a database containing all previous members must be queried. Using a
    hash table, this can be done in *0(1)* time for each element, but elements are 
    never discarded, resulting in *O(n)* space complexity.

## Proposed Solution:

    While we don't know if the sequence injects the natural numbers, we do know that
    large ranges will be accounted for. Applying this knowledge, large ranges can be
    represented with a single integer or tuple.

        **Inserting**

            - Each new value is stored in a base-level hash table T<sub>1<\sub>,
            - When a range, R<sub>1,1<\sub> is filled, R<sub>1,1<\sub> is stored as an integer or tuple in the next level hash table T<sub>2<\sub>.
            - When a large range of ranges R<sub>2,1<\sub> is filled, it is stored in the next level hash T<sub>3<\sub>.
            - this pattern may continue indefinitely.

        **Querying**

            - The value is first queried against the highest level hash table T<sub>m<\sub>
            - If not found, it is then queried against H<sub>m-1<\sub>
            - This continues to T<sub>1<\sub>
