meanArray = c(0.32,0.26,0.24,0.26,0.27,0.25)
sd(meanArray)
#normal names:
#names(meanArray) = c("ml_minimal", "ml_stripped","ml","ml_advancedSimple","ml_advanced","ml_combined")
names(meanArray) = c("minimal", "stripped","ml","enriched","advanced","combined")
bot = c("Rdeep")
barplot(meanArray,names.arg =names(meanArray),ylim = c(0,0.4),ylab = "Part of games won", xpd = FALSE,main = paste("Part of games won against ",bot))
