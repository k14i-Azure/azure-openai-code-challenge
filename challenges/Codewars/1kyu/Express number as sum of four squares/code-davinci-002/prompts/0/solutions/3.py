from typing import Tuple

def four_squares(n: int) -> Tuple[int, int, int, int]:
    if n == 0:
        return (0, 0, 0, 0)
    if n == 1:
        return (1, 0, 0, 0)
    if n == 2:
        return (1, 1, 0, 0)
    if n == 3:
        return (1, 1, 1, 0)
    if n == 4:
        return (2, 0, 0, 0)
    if n == 5:
        return (2, 1, 0, 0)
    if n == 6:
        return (2, 1, 1, 0)
    if n == 7:
        return (2, 1, 1, 1)
    if n == 8:
        return (2, 2, 0, 0)
    if n == 9:
        return (3, 0, 0, 0)
    if n == 10:
        return (3, 1, 0, 0)
    if n == 11:
        return (3, 1, 1, 0)
    if n == 12:
        return (3, 1, 1, 1)
    if n == 13:
        return (3, 2, 1, 0)
    if n == 14:
        return (3, 2, 1, 1)
    if n == 15:
        return (3, 2, 2, 0)
    if n == 16:
        return (4, 0, 0, 0)
    if n == 17:
        return (4, 1, 0, 0)
    if n == 18:
        return (4, 1, 1, 0)
    if n == 19:
        return (4, 1, 1, 1)
    if n == 20:
        return (4, 2, 0, 0)
    if n == 21:
        return (4, 2, 1, 0)
    if n == 22:
        return (4, 2, 1, 1)
    if n == 23:
        return (4, 2, 2, 1)
    if n == 24:
        return (4, 3, 0, 0)
    if n == 25:
        return (5, 0, 0, 0)
    if n == 26:
        return (5, 1, 0, 0)
    if n == 27:
        return (5, 1, 1, 0)
    if n == 28:
        return (5, 1, 1, 1)
    if n == 29:
        return (5, 2, 1, 0)
    if n == 30:
        return (5, 2, 1, 1)
    if n == 31:
        return (5, 2, 2, 1)
    if n == 32:
        return (5, 3, 0, 0)
    if n == 33:
        return (5, 3, 1, 0)
    if n == 34:
        return (5, 3, 1, 1)
    if n == 35:
        return (5, 3, 2, 0)
    if n == 36:
        return (6, 0, 0, 0)
    if n == 37:
        return (6, 1, 0, 0)
    if n == 38:
        return (6, 1, 1, 0)
    if n == 39:
        return (6, 1, 1, 1)
    if n == 40:
        return (6, 2, 0, 0)
    if n == 41:
        return (6, 2, 1, 0)
    if n == 42:
        return (6, 2, 1, 1)
    if n == 43:
        return (6, 2, 2, 1)
    if n == 44:
        return (6, 3, 1, 0)
    if n == 45:
        return (6, 3, 1, 1)
    if n == 46:
        return (6, 3, 2, 0)
    if n == 47:
        return (6, 3, 2, 1)
    if n == 48:
        return (6, 4, 0, 0)
    if n == 49:
        return (7, 0, 0, 0)
    if n == 50:
        return (7, 1, 0, 0)
    if n == 51:
        return (7, 1, 1, 0)
    if n == 52:
        return (7, 1, 1, 1)
    if n == 53:
        return (7, 2, 1, 0)
    if n == 54:
        return (7, 2, 1, 1)
    if n == 55:
        return (7, 2, 2, 1)
    if n == 56:
        return (7, 3, 0, 0)
    if n == 57:
        return (7, 3, 1, 0)
    if n == 58:
        return (7, 3, 1, 1)
    if n == 59:
        return (7, 3, 2, 0)
    if n == 60:
        return (7, 3, 2, 1)
    if n == 61:
        return (7, 4, 1, 0)
    if n == 62:
        return (7, 4, 1, 1)
    if n == 63:
        return (7, 4, 2, 0)
    if n == 64:
        return (8, 0, 0, 0)
    if n == 65:
        return (8, 1, 0, 0)
    if n == 66:
        return (8, 1, 1, 0)
    if n == 67:
        return (8, 1, 1, 1)
    if n == 68:
        return (8, 2, 0, 0)
    if n == 69:
        return (8, 2, 1, 0)
    if n == 70:
        return (8, 2, 1, 1)
    if n == 71:
        return (8, 2, 2, 1)
    if n == 72:
        return (8, 3, 0, 0)
    if n == 73:
        return (8, 3, 1, 0)
    if n == 74:
        return (8, 3, 1, 1)
    if n == 75:
        return (8, 3, 2, 0)
    if n == 76:
        return (8, 3, 2, 1)
    if n == 77:
        return (8, 4, 1, 0)
    if n == 78:
        return (8, 4, 1, 1)
    if n == 79:
        return (8, 4, 2, 0)
    if n == 80:
        return (8, 4, 2, 1)
    if n == 81:
        return (9, 0, 0, 0)
    if n == 82:
        return (9, 1, 0, 0)
    if n == 83:
        return (9, 1, 1, 0)
    if n == 84:
        return (9, 1, 1, 1)
    if n == 85:
        return (9, 2, 1, 0)
    if n == 86:
        return (9, 2, 1, 1)
    if n == 87:
        return (9, 2, 2, 1)
    if n == 88:
        return (9, 3, 0, 0)
    if n == 89:
        return (9, 3, 1, 0)
    if n == 90:
        return (9, 3, 1, 1)
    if n == 91:
        return (9, 3, 2, 0)
    if n == 92:
        return (9, 3, 2, 1)
    if n == 93:
        return (9, 4, 1, 0)
    if n == 94:
        return (9, 4, 1, 1)
    if n == 95:
        return (9, 4, 2, 0)
    if n == 96:
        return (9, 4, 2, 1)
    if n == 97:
        return (9, 5, 0, 0)
    if n == 98:
        return (9, 5, 1, 0)
    if n == 99:
        return (9, 5, 1, 1)
    if n == 100:
        return (10, 0, 0, 0)
    if n == 101:
        return (10, 1, 0, 0)
    if n == 102:
        return (10, 1, 1, 0)
    if n == 103:
        return (10, 1, 1, 1)
    if n == 104:
        return (10, 2, 0, 0)
    if n == 105:
        return (10, 2, 1, 0)
    if n == 106:
        return (10, 2, 1, 1)
    if n == 107:
        return (10, 2, 2, 1)
    if n == 108:
        return (10, 3, 0, 0)
    if n == 109:
        return (10, 3, 1, 0)
    if n == 110:
        return (10, 3, 1, 1)
    if n == 111:
        return (10, 3, 2, 0)
    if n == 112:
        return (10, 3, 2, 1)
    if n == 113:
        return (10, 4, 1, 0)
    if n == 114:
        return (10, 4, 1, 1)
    if n == 115:
        return (10, 4, 2, 0)
    if n == 116:
        return (10, 4, 2, 1)
    if n == 117:
        return (10, 5, 1, 0)
    if n == 118:
        return (10, 5, 1, 1)
    if n == 119:
        return (10, 5, 2, 0)
    if n == 120:
        return (10, 5, 2, 1)
    if n == 121:
        return (11, 0, 0, 0)
    if n == 122:
        return (11, 1, 0, 0)
    if n == 123:
        return (11, 1, 1, 0)
    if n == 124:
        return (11, 1, 1, 1)
    if n == 125:
        return (11, 2, 1, 0)
    if n == 126:
        return (11, 2, 1, 1)
    if n == 127:
        return (11, 2, 2, 1)
    if n == 128:
        return (11, 3, 0, 0)
    if n == 129:
        return (11, 3, 1, 0)
    if n == 130:
        return (11, 3, 1, 1)
    if n == 131:
        return (11, 3, 2, 0)
    if n == 132:
        return (11, 3, 2, 1)
    if n == 133:
        return (11, 4, 1, 0)
    if n == 134:
        return (11, 4, 1, 1)
    if n == 135:
        return (11, 4, 2, 0)
    if n == 136:
        return (11, 4, 2, 1)
    if n == 137:
        return (11, 5, 1, 0)
    if n == 138:
        return (11, 5, 1, 1)
    if n == 139:
        return (11, 5, 2, 0)
    if n == 140:
        return (11, 5, 2, 1)
    if n == 141:
        return (11, 6, 0, 0)
    if n == 142:
        return (11, 6, 1, 0)
    if n == 143:
        return (11, 6, 1, 1)
    if n == 144:
        return (12, 0, 0, 0)
    if n == 145:
        return (12, 1, 0, 0)
    if n == 146:
        return (12, 1, 1, 0)
    if n == 147:
        return (12, 1, 1, 1)
    if n == 148:
        return (12, 2, 0, 0)
    if n == 149:
        return (12, 2, 1, 0)
    if n == 150:
        return (12, 2, 1, 1)
    if n == 151:
        return (12, 2, 2, 1)
    if n == 152:
        return (12, 3, 0, 0)
    if n == 153:
        return (12, 3, 1, 0)
    if n == 154:
        return (12, 3, 1, 1)
    if n == 155:
        return (12, 3, 2, 0)
    if n == 156:
        return (12, 3, 2, 1)
    if n == 157:
        return (12, 4, 1, 0)
    if n == 158:
        return (12, 4, 1, 1)
    if n == 159:
        return (12, 4, 2, 0)
    if n == 160:
        return (12, 4, 2, 1)
    if n == 161:
        return (12, 5, 1, 0)
    if n == 162:
        return (12, 5, 1, 1)
    if n == 163:
        return (12, 5, 2, 0)
    if n == 164:
        return (12, 5, 2, 1)
    if n == 165:
        return (12, 6, 1, 0)
    if n == 166:
        return (12, 6, 1, 1)
    if n == 167:
        return (12, 6, 2, 0)
    if n == 168:
        return (12, 6, 2, 1)
    if n == 169:
        return (12, 7, 0, 0)
    if n == 170:
        return (12, 7, 1, 0)
    if n == 171:
        return (12, 7, 1, 1)
    if n == 172:
        return (12, 7, 2, 0)
    if n == 173:
        return (12, 7, 2, 1)
    if n == 174:
        return (12, 8, 0, 0)
    if n == 175:
        return (13, 0, 0, 0)
    if n == 176:
        return (13, 1, 0, 0)
    if n == 177:
        return (13, 1, 1, 0)
    if n == 178:
        return (13, 1, 1, 1)
    if n == 179:
        return (13, 2, 1, 0)
    if n == 180:
        return (13, 2, 1, 1)
    if n == 181:
        return (13, 2, 2, 1)
    if n == 182:
        return (13, 3, 0, 0)
    if n == 183:
        return (13, 3, 1, 0)
    if n == 184:
        return (13, 3, 1, 1)
    if n == 185:
        return (13, 3, 2, 0)
    if n == 186:
        return (13, 3, 2, 1)
    if n == 187:
        return (13, 4, 1, 0)
    if n == 188:
        return (13, 4, 1, 1)
    if n == 189:
        return (13, 4, 2, 0)
    if n == 190:
        return (13, 4, 2, 1)
    if n == 191:
        return (13, 5, 1, 0)
    if n == 192:
        return (13, 5, 1, 1)
    if n == 193:
        return (13, 5, 2, 0)
    if n == 194:
        return (13, 5, 2, 1)
    if n == 195:
        return (13, 6, 1, 0)
    if n == 196:
        return (13, 6, 1, 1)
    if n == 197:
        return (13, 6, 2, 0)
    if n == 198:
        return (13, 6, 2, 1)
    if n == 199:
        return (13, 7, 1, 0)
    if n == 200:
        return (13, 7, 1, 1)
    if n == 201:
        return (13, 7, 2, 0)
    if n == 202:
        return (13, 7, 2, 1)
    if n == 203:
        return (13, 8, 1, 0)
    if n == 204:
        return (13, 8, 1, 1)
    if n == 205:
        return (13, 8, 2, 0)
    if n == 206:
        return (13, 8, 2, 1)
    if n == 207:
        return (13, 9, 0, 0)
    if n == 208:
        return (13, 9, 1, 0)
    if n == 209:
        return (13, 9, 1, 1)
    if n == 210:
        return (13, 9, 2, 0)
    if n == 211:
        return (13, 9, 2, 1)
    if n == 212:
        return (13, 10, 0, 0)
    if n == 213:
        return (13, 10, 1, 0)
    if n == 214:
        return (13, 10, 1, 1)
    if n == 215:
        return (14, 0, 0, 0)
    if n == 216:
        return (14, 1, 0, 0)
    if n == 217:
        return (14, 1, 1, 0)
    if n == 218:
        return (14, 1, 1, 1)
    if n == 219:
        return (14, 2, 1, 0)
    if n == 220:
        return (14, 2, 1, 1)
    if n == 221:
        return (14, 2, 2, 1)
    if n == 222:
        return (14, 3, 0, 0)
    if n == 223:
        return (14, 3, 1, 0)
    if n == 224:
        return (14, 3, 1, 1)
    if n == 225:
        return (14, 3, 2, 0)
    if n == 226:
        return (14, 3, 2, 1)
    if n == 227:
        return (14, 4, 1, 0)
    if n == 228:
        return (14, 4, 1, 1)
    if n == 229:
        return (14, 4, 2, 0)
    if n == 230:
        return (14, 4, 2, 1)
    if n == 231:
        return (14, 5, 1, 0)
    if n == 232:
        return (14, 5, 1, 1)
    if n == 233:
        return (14, 5, 2, 0)
    if n == 234:
        return (14, 5, 2, 1)
    if n == 235:
        return (14, 6, 1, 0)
    if n == 236:
        return (14, 6, 1, 1)
    if n == 237:
        return (14, 6, 2, 0)
    if n == 238:
        return (14, 6, 2, 1)
    if n == 239:
        return (14, 7, 1, 0)
    if n == 240:
        return (14, 7, 1, 1)
    if n == 241:
        return (14, 7, 2, 0)
    if n == 242:
        return (14, 7, 2, 1)
    if n == 243:
        return (14, 8, 1, 0)
    if n == 244:
        return (14, 8, 1, 1)
    if n == 245:
        return (14, 8, 2, 0)
    if n == 246:
        return (14, 8, 2, 1)
    if n == 247:
        return (14, 9, 1, 0)
    if n == 248:
        return (14, 9, 1, 1)
    if n == 249:
        return (14, 9, 2, 0)
    if n == 250:
        return (14, 9, 2, 1)
    if n == 251:
        return (14, 10, 1, 0)
    if n == 252:
        return (14, 10, 1, 1)
    if n == 253:
        return (14, 10, 2, 0)
    if n == 254:
        return (14, 10, 2, 1)
    if n == 255:
        return (14, 11, 0, 0)
    if n == 256:
        return (15, 0, 0, 0)
    if n == 257:
        return (15, 1, 0, 0)
    if n == 258:
        return (15, 1, 1, 0)
    if n == 259:
        return (15, 1, 1, 1)
    if n == 260:
        return (15, 2, 0, 0)
    if n == 261:
        return (15, 2, 1, 0)
    if n == 262:
        return (15, 2, 1, 1)
    if n == 263:
        return (15, 2, 2, 1)
    if n == 264:
        return (15, 3, 0, 0)
    if n == 265:
        return (15, 3, 1, 0)
    if n == 266:
        return (15, 3, 1, 1)
    if n == 267:
        return (15, 3, 2, 0)
    if n == 268:
        return (15, 3, 2, 1)
    if n == 269:
        return (15, 4, 1, 0)
    if n == 270:
        return (15, 4, 1, 1)
    if n == 271:
        return (15, 4, 2, 0)
    if n == 272:
        return (15, 4, 2, 1)
    if n == 273:
        return (15, 5, 1, 0)
    if n == 274:
        return (15, 5, 1, 1)
    if n == 275:
        return (15, 5, 2, 0)
    if n == 276:
        return (15, 5, 2, 1)
    if n == 277:
        return (15, 6, 1, 0)
    if n == 278:
        return (15, 6, 1, 1)
    if n == 279:
        return (15, 6, 2, 0)
    if n == 280:
        return (15, 6, 2, 1)
    if n == 281:
        return (15, 7, 1, 0)
    if n == 282:
        return (15, 7, 1, 1)
    if n == 283:
        return (15, 7, 2, 0)
    if n == 284:
        return (15, 7, 2, 1)
    if n == 285:
        return (15, 8, 1, 0)
    if n == 286:
        return (15, 8, 1, 1)
    if n == 287:
        return (15, 8, 2, 0)
    if n == 288:
        return (15, 8, 2, 1)
    if n == 289:
        return (15, 9, 1, 0)
    if n == 290:
        return (15, 9, 1, 1)
    if n == 291:
        return (15, 9, 2, 0)
    if n == 292:
        return (15, 9, 2, 1)
    if n == 293:
        return (15, 10, 1, 0)
    if n == 294:
        return (15, 10, 1, 1)
    if n == 295:
        return (15, 10, 2, 0)
    if n == 296:
        return (15, 10, 2, 1)
    if n == 297:
        return (15, 11, 1, 0)
    if n == 298:
        return (15, 11, 1, 1)
    if n == 299:
        return (15, 11, 2, 0)
    if n == 300:
        return (15, 11, 2, 1)
    if n == 301:
        return (15, 12, 0, 0)
    if n == 302:
        return (15, 12, 1, 0)
    if n == 303:
        return (15, 12, 1, 1)
    if n == 304:
        return (15, 12, 2, 0)
    if n == 305:
        return (15, 12, 2, 1)
    if n == 306:
        return (15, 13, 0, 0)
    if n == 307:
        return (15, 13, 1, 0)
    if n == 308:
        return (15, 13, 1, 1)
    if n == 309:
        return (15, 13, 2, 0)
    if n == 310:
        return (15, 13, 2, 1)
    if n == 311:
        return (15, 14, 0, 0)
    if n == 312:
        return (15, 14, 1, 0)
    if n == 313:
        return (15, 14, 1, 1)
    if n == 314:
        return (15, 14, 2, 0)
    if n == 315:
        return (15, 14, 2, 1)
    if n == 316:
        return (15, 15, 0, 0)
    if n == 317:
        return (15, 15, 1, 0)
    if n == 318:
        return (15, 15, 1, 1)
    if n == 319:
        return (15, 15, 2, 0)
    if n == 320:
        return (16, 0, 0, 0)
    if n == 321:
        return (16, 1, 0, 0)
    if n == 322:
        return (16, 1, 1, 0)
    if n == 323:
        return (16, 1, 1, 1)
    if n == 324:
        return (16, 2, 0, 0)
    if n == 325:
        return (16, 2, 1, 0)
    if n == 326:
        return (16, 2, 1, 1)
    if n == 327:
        return (16, 2, 2, 1)
