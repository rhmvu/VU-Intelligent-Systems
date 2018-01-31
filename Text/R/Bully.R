meanArray = c(0.78,0.78,0.81,0.71,0.75,0.70)
              

#normal names:
#names(meanArray) = c("ml_minimal", "ml_stripped","ml","ml_advancedSimple","ml_advanced","ml_combined")
names(meanArray) = c("minimal", "stripped","ml","enriched","advanced","combined")
bot = c("Bully")
barplot(meanArray,names.arg =names(meanArray),ylim = c(0.6,1.0),ylab = "Part of games won", xpd = FALSE,main = paste("Part of games won against ",bot))
