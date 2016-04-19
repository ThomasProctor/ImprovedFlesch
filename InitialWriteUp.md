# Title

## What I did

The Flesch-Kincaid readability tests are tests designed to indicate the ease of reading a passage of English text.
The most common form is the Flesch-Kincaid grade level, which assigns a text a grade level that corresponds to the grades in American primary and secondary school.
For those who aren't familiar with the American school system, it is basically an integer that corresponds with total years of schooling.

However, the reading level is based mostly around two measures: the number of words in each sentence, and the number of syllables in each word.
My basic idea for this project is that counting the number of syllables in a word does not actually correspond with how difficult it is to read. 
Instead, it is whether the reader is familiar with the word.
With Flesch-Kincaid, the words "congeal" and "about" are assinged the same reading difficulty.
However, many readers might have no idea what "congeal" means, while any native English speaker is familiar with the meanin of "about".

I decided that a better proxy for the common familiarity with a word would be how much it is commonly used.
This is something I can find by looking at frequency counts of words in a corpus of the english language.

## Conclusions

The biggest problem currently? The corpus. The Brown Corpus is old. It doesn't 
contain words like taxi and smartphone.
Also, it's small.
There are lots of words that just get relegated to the not showing up in the corpus category.

These are words that most people who are reading my test document would 
understand no problem. 
This could probably be fixed by replacing the corpus with a newer and larger one.
I could probably mine twitter for some nice, casual language, but that would be
a big project all by itself.

Next, I should probably just look at the roots of words.
Right now, "do", "does" and "doesn't" all have different grade levels.
They should probably all be the same grade level.
I could run the frequency count and the document through a stemmer.
Each word would be reduced to its stem and counted in the frequency dictionary as the stem.
This would combine the frequency counts into one word.
Then when reading to document, words would be stemmed for dictionary look-up as well.
It wouldn't be a perfect solution though.
For example, "rebirth" is much less common and harder to understand than 
"birth", but both would count as the same word.

Unfortunately, this whole task migh be pointless.
The [IRS thinks that syllables are actually the most important part of reading level.](http://www.npr.org/2016/03/31/472500987/how-to-make-tax-forms-easier-break-the-math-up-one-step-per-line "NPR interview with Bob Erickson")
They take it so seriously that they replace long word combination with acronyms.
Even if people are not familiar with the acronym and have to look it up, it is
they think it is still easier to read.
Of course it could be that they are just blindly following the Flesch-Kincaid.

One thing that could be useful regardless is using this approach for Chinese.
Using Flesch-Kincaid directly on Chinese text is hard.
Syllables can't be extracted from the text.
Even if they could be, there are a bunch of different Chinese languages 
represented with the same Chinese writing.
Depending on the language of the speaker, the word represented by a syllable might have a different number of syllables.
Furthermore, in the most common Chinese language, Mardarin Chinese, most all lexemes are single syllables.
Thus looking at syllables wouldn't be useful.
If one had a Chinese corpus though, you could easily apply my approach to it to generate a grade reading level.


 - Corpus is pretty small. This makes it not quite as useful.
 - Probably should run all words through a stemmer.
 - Some people seem to think that the syllable thing is actually a big deal.	
