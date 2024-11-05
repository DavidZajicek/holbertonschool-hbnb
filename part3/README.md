-- General notes --
Notice that for the models, the value assignment statements in the constructor differ from the ones in the setter.
e.g. self.description = description  VS  self._description = value

The one in the constructor is actually calling the setter, and the one in the setter is actually saving the value to the internal _description attribute. The name shown to the outside world is actually invoking the getters and setters while internally the attribute's name has an underscore prefix.


-- Base model --
In the documentation, there is a brief mention of using the BaseModel class and inheriting from it. My code does not do this so you will see the uuid, last_created and last_updated attributes appear again and again in every model.
To be honest, whether you want to inherit from a class or not is up to you. The advantage is that it reduces the number of things you need to type and makes code maintennence easier, but it may also be a pain-in-the-behind if the code changes frequently and you have to update two places regularly instead of just one.


-- User model --
Pretty straight forward for most of the model. Note that a very simple regular expression is used to validate the email address.

The two static methods in the model (email_exists, user_exists) have hardcoded return values for now because at this point we haven't designed how all the User objects are going to be stored and thus have no proper way of searching through all of them to find the data we need.


-- Place model --
Similar in structure to the other models and has a LOT of attributes.

There is one static method to take note of (place_exists) and this one has a hardcoded return value too because at this point there is no proper design as to how all the Place objects are to be organised in the system.


-- Review model --
Nothing special.


-- Amenity model --
Nothing special.


-- Tests --
The way I wrote my tests is slightly different from the example code in the project but it still works.

Fomr the command line, make sure you are in the 'app' folder, then run the following: python3 -m unittest tests/test_user.py

-- Mermaid Diagram --
[![](https://mermaid.ink/img/pako:eNqVVG1r2zAQ_iuHPm2QjG6QD_O3snlQso7QptsKBiNbl1ggS0Y6LSup__suL7WduN062R_O99zLc9JjbUXpFIpEoP-s5drLOrOZBV53t-kNPD5Op24Li6-Xn1JIwG1sGKM36fer9AfDTSyMDhUeYw5Z50GVPIFb13fIL6_Tb1fL-2HUk-tvcYeno7U92LsVo1bA72Le-wJ5bddvPsxmb2GlfaDcyhrPcTDyJQRrqQ3cjUpCI0PYOK8gE8yrQpWJPqZwzoAOuVS1PrJthxvxKtZAmsyYkcJQet2QdrbHFJa6lgYar0tkSnUMBAWChMYFTfoXgo11gX7IcmWcJJ6d-0Q1zCqQNogWph8v3l2AtAp2xjOpzq7_P3c_MasLfc7Gl_nJ_hyl848NWqY_l0D4m3qXtgSeR-EdysT76WzUMYbThh3QGFniM1SehPe6w9qpp9PJ8LDzl-p0fRfzyYgUV7OaHs7gdqd9MRE1etal4l95XzQTVCGLVyRsKlzJaGg3f8uhMpK7fbClSMhHnAjv4roSyUqawF-xUZLweBt0XlSanL8-XBb7O6P9A1ykQck?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNqVVG1r2zAQ_iuHPm2QjG6QD_O3snlQso7QptsKBiNbl1ggS0Y6LSup__suL7WduN062R_O99zLc9JjbUXpFIpEoP-s5drLOrOZBV53t-kNPD5Op24Li6-Xn1JIwG1sGKM36fer9AfDTSyMDhUeYw5Z50GVPIFb13fIL6_Tb1fL-2HUk-tvcYeno7U92LsVo1bA72Le-wJ5bddvPsxmb2GlfaDcyhrPcTDyJQRrqQ3cjUpCI0PYOK8gE8yrQpWJPqZwzoAOuVS1PrJthxvxKtZAmsyYkcJQet2QdrbHFJa6lgYar0tkSnUMBAWChMYFTfoXgo11gX7IcmWcJJ6d-0Q1zCqQNogWph8v3l2AtAp2xjOpzq7_P3c_MasLfc7Gl_nJ_hyl848NWqY_l0D4m3qXtgSeR-EdysT76WzUMYbThh3QGFniM1SehPe6w9qpp9PJ8LDzl-p0fRfzyYgUV7OaHs7gdqd9MRE1etal4l95XzQTVCGLVyRsKlzJaGg3f8uhMpK7fbClSMhHnAjv4roSyUqawF-xUZLweBt0XlSanL8-XBb7O6P9A1ykQck)