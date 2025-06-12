#!/bin/bash

# Verifica que se proporcionen los argumentos correctos
if [ $# -ne 2 ]; then
    echo "Uso: $0 <nombre_imagen> <nuevo_sha>"
    echo "Ejemplo: $0 module.dashboard/backendv2 123456789abcdef"
    exit 1
fi

# Extrae los argumentos
IMAGE_NAME="$1"
NEW_SHA="$2"

# Escapa caracteres especiales para sed
IMAGE_NAME_ESCAPED=$(echo "$IMAGE_NAME" | sed 's/[\/&]/\\&/g')

# Busca el archivo que contiene la imagen
FILE=$(find . -type f -name "*.yaml" -exec grep -l "${IMAGE_NAME_ESCAPED}:" {} \;)

if [ -z "$FILE" ]; then
    echo "Error: No se encontró ningún archivo que contenga la imagen ${IMAGE_NAME}"
    exit 1
fi

# Muestra el archivo encontrado
echo "Archivo encontrado: $FILE"

# Realiza el reemplazo usando sed
sed -i "s/\(.*${IMAGE_NAME_ESCAPED}:\)[^[:space:]]*/\1${NEW_SHA}/" "$FILE"

# Verifica si el reemplazo fue exitoso
grep -q "${IMAGE_NAME}:${NEW_SHA}" "$FILE"
if [ $? -eq 0 ]; then
    echo "SHA actualizado exitosamente a ${NEW_SHA}"
else
    echo "Error: No se pudo actualizar el SHA"
    exit 1
fi
