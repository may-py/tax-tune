Hi Friends,

I have followed videos of Corey Schafer to do this proejct and I have completed 12 tutorials. 
Link of course: https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

While doing this project I met an issues that I would like to update here.


1) Login error after Delete Profile picture from Admin: 
  - Error 1:RelatedObjectDoesNotExist at /admin/login/, no such column: user_details_profile.id
    - Solution: https://stackoverflow.com/questions/52244032/i-keep-getting-relatedobjectdoesnotexist-at-admin-login-how-do-i-successfully
  - Error 2: Exception Value: save() got an unexpected keyword argument 'force_insert'
    - Solution: https://stackoverflow.com/questions/58157297/type-error-save-got-an-unexpected-keyword-argument-force-insert
    
    
2) I did mistake in date_posted line code of blog models.
  - Solution code: timezone.now instead of timezone.now()
